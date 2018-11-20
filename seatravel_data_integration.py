from pymongo import MongoClient
import time
from json import loads
import requests
import traceback
from validation import validation
import log
import usedforId_producer

logger = log.get_logger('validation_seatravel')
facility_logger = log.get_logger('facility_seatravel')

client = MongoClient('185.44.36.51', 27018)
db = client.Monitoring


class SeatravelMappingProccess:
    def __init__(self, dictionary):
        self.facilities = {}
        self.remaining_facility = []
        self.dictionary = dictionary
        self.giata = ''

    def info_seatravel(self):
        def get_info(i, token, item):
            try:
                url = "http://service.seatravel.com.tr/v2/api/productservice/getproductInfo"
                payload = {
                    "culture": "en-US",
                    "ownerProvider": 2,
                    "productType": 2,
                    "product": i
                }
                payload = str(payload)
                headers = {
                    'content-type': "application/json",
                    'authorization': "Bearer " + token,
                }
                response = requests.request("POST", url, data=payload, headers=headers)
                response = response.text
                response = (loads(response))
                try:
                    item["informationn"] = response["body"]['hotel']
                    db.arezootest.save(item)
                    # print("/-------------------------ok save--->id: " + i + " ---------------------------/")
                except:
                    pass
            except:
                db.seatravelinfo_error.insert({"err": str(traceback.format_exc()), "id": i})

        try:
            url2 = "http://service.seatravel.com.tr/v2/api/authenticationservice/login"

            payload2 = "{\r\n  \"Agency\" : \"AMT\",  \r\n  \"User\" : \"AMITIS1\", \r\n  \"Password\" : \"amt3029\" \r\n}"
            headers2 = {
                'content-type': "application/json",

            }
            response2 = requests.request("POST", url2, data=payload2, headers=headers2)
            response2 = response2.text
            response2 = loads(response2)
            token = (response2)["body"]["token"]
            for item in list(db.arezootest.find({})):
                get_info(str(item["Id"]), token, item)
                time.sleep(2)

        except:
            time.sleep(20)
            url2 = "http://service.seatravel.com.tr/v2/api/authenticationservice/login"

            payload2 = "{\r\n  \"Agency\" : \"AMT\",  \r\n  \"User\" : \"AMITIS1\", \r\n  \"Password\" : \"amt3029\" \r\n}"
            headers2 = {
                'content-type': "application/json",

            }

            response2 = requests.request("POST", url2, data=payload2, headers=headers2)
            response2 = response2.text
            response2 = loads(response2)
            token = (response2)["body"]["token"]
            for item in list(db.arezootest.find({})):
                get_info(str(item["Id"]), token, item)
                time.sleep(2)

    def get_hotel_info(self):
        hotel_list = db.test.find_one({"mark": None})
        city = None
        country = None
        try:
            city_seatravel = hotel_list["informationn"]["city"]["id"]
            city = db.city.find_one({"ws.23": city_seatravel})
        except:
            city = None
        try:
            country_seatravel = hotel_list["informationn"]["country"]["id"]
            country = db.country.find_one({"ws.23": country_seatravel})
        except:
            country = None
        self.giata = hotel_list["GiataId"]
        return {"hotellist": hotel_list, "id": hotel_list["Id"], "city": {"title": city["title"], "id": city["id"]}, "country": {"title": country["title"], "id": country["id"]}}

    def set_value_basis(self, info):
        obj = {}
        new = {}
        for key, value in (self.dictionary['schema_m1']['dictionary']).items():

            try:
                obj[key] = validation(key, eval(value["path"]), value["typeid"])
                if value["optional"] == 0 and obj[key] == None:
                    logger.info(f'****deleted_hotel_seatravel****:{info}')
                    return
            except:
                obj[key] = ''
            if obj[key] != None and obj[key] != '':
                new[key] = obj[key]
        return new

    def add_mark_collection(self, id):
        db.test.update_many({"Id": id}, {'$set': {'mark': 1}})

    def get_facility_hotel(self, hotel):
        try:
            facilities = hotel["informationn"]["seasons"][0]["facilityCategories"][0]["facilities"]
            facilities = [i["name"] for i in facilities]
        except:
            facilities = None
        if facilities:
            self.facilities = facilities
        else:
            self.facilities = None
        return self.facilities

    def set_facility_value(self, hotel, hotel_info):
        self.get_facility_hotel(hotel)
        if self.facilities == None:
            return None
        hotel_facility = [self.dictionary['schema_m1']['facilities'][item] for item in self.facilities if item in self.dictionary['schema_m1']['facilities']]
        total_basis_facilities = {}
        for fixed_item in self.dictionary['schema_m1']['fixed_list']:
            for title, options in fixed_item.items():
                common_facility = list(set(hotel_facility).intersection(options))
                if len(common_facility) != 0:
                    total_basis_facilities = set(total_basis_facilities) | set(common_facility)
                    hotel_info[title] = common_facility
        # print(total_basis_facilities)
        remaining = (set(hotel_facility)) - total_basis_facilities
        self.remaining_facility.extend({"facility": remaining, "id": hotel["Id"]})
        return hotel_info

    def finding_usedforid(self):

        used_for_id = db.giata_with_basis_id.find_one({'giata': int(self.giata)})['basis_id']
        method = 'update'
        if used_for_id == 0:
            used_for_id = usedforId_producer.produce_usedforid()
            # used_for_id = '1234'
            db.giata_with_basis_id.update({"giata": int(self.giata)}, {'$set': {'basis_id': int(used_for_id)}})
            method = 'insert'
        return used_for_id, method

    def export_data(self):
        result = []
        hotelinfo = self.get_hotel_info()
        temp_result = self.set_value_basis(hotelinfo["hotellist"])
        if temp_result:
            used_for_id, method = self.finding_usedforid()
            temp_result_facility = self.set_facility_value(hotelinfo["hotellist"], temp_result)
            if temp_result_facility == None:
                pass
            else:
                temp_result = temp_result_facility
            temp_result.update({"city": hotelinfo["city"], "country": hotelinfo["country"], "usedForID": used_for_id, "method": method})

        facility_logger.info(f'the facilities do not exist in basisCore: {set(self.remaining_facility)}')
        # self.add_mark_collection(hotelinfo["id"])
        return temp_result
