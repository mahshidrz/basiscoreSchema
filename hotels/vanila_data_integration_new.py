import traceback
import webbrowser
import time
import glob
import json
import requests
import xmltodict
from pymongo import MongoClient
from bson import ObjectId
from validation import validation
import log
import usedforId_producer

client = MongoClient('185.44.36.51', 27018)
db = client.Monitoring

# client = MongoClient('localhost', 27017)
# db = client.ticketlist

logger = log.get_logger('validation')
facility_logger = log.get_logger('facility')


class VanilaMappingProccess:
    def __init__(self, dictionary):
        super(VanilaMappingProccess, self)
        self.hotel_id_list = []
        self.remaining_facility = []
        self.dictionary = dictionary
        self.giata_code = None
        self.hotel_id = None

    def get_city_info(self, city_id):
        try:
            city_info = db.city.find_one({'ws.10': city_id, 'lid': 2}, {'id': 1, 'title': 1, '_id': 0})
            return {'title': city_info['title'], 'id': city_info['id']}
        except:
            return {}

    def get_country_info(self, country_id):
        try:
            country_info = db.country.find_one({'ws.10': country_id, 'lid': 2}, {'id': 1, 'title': 1, '_id': 0})
            return {'title': country_info['title'], 'id': country_info['id']}
        except:
            return {}

    def update_hotels(self):
        old_col_hotel = list(db.vanila_hotel_list.find({}, {'HotelId': 1, '_id': 0}))
        old_col_hotel = [id['HotelId'] for id in old_col_hotel]

        new_col_hotel = list(db.vanila_hotel_list_final.find({}, {'HotelId': 1, '_id': 0}))
        new_col_hotel = [id['HotelId'] for id in new_col_hotel]

        difference_hotels = set(new_col_hotel) - set(old_col_hotel)

        find_difference_hotel = list(db.vanila_hotel_list_final.find({'HotelId': {'$in': list(difference_hotels)}}))
        db.vanila_hotel_list.insert_many(find_difference_hotel)

    def get_hotel_details(self, hotelid):
        url = "http://leont.leonardotravel.com/Static.svc/wsdl"
        querystring = {"wsdl": ""}
        payload = "<!--<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\">-->\r\n<!--  <s:Body>-->\r\n<!--    <HotelDetail xmlns=\"http://tempuri.org/\">-->\r\n<!--      <Header>-->\r\n<!--        <AgentId>26651</AgentId>-->\r\n<!--        <Username>xml.F.SHAREI@LACHINSEIR.COM</Username>-->\r\n<!--        <Password>123456</Password>-->\r\n<!--      </Header>-->\r\n<!--      <Hotel>-->\r\n<!--        <HotelId>" + str(
            hotelid) + "</HotelId>-->\r\n<!--        <Language>En</Language>-->\r\n<!--      </Hotel>-->\r\n<!--    </HotelDetail>-->\r\n<!--  </s:Body>-->\r\n<!--</s:Envelope>-->\r\n\r\n\r\n<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\">\r\n<s:Body>\r\n<HotelDetail xmlns=\"http://tempuri.org/\">\r\n<Header>\r\n<AgentId>26651</AgentId>\r\n<Password>123456</Password>\r\n<Username>xml.F.SHAREI@LACHINSEIR.COM</Username>\r\n</Header><Hotel>\r\n<HotelId>" + str(
            hotelid) + "</HotelId>\r\n<Language>En</Language>\r\n</Hotel>\r\n</HotelDetail>\r\n</s:Body>\r\n</s:Envelope>"
        headers = {
            'SOAPAction': "http://tempuri.org/IStatic/HotelDetail",
            'ContentType': "text/xml; charset=utf-8",
            'Content-Type': "text/xml",
            'Cache-Control': "no-cache",

        }
        try:
            response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
            response = json.loads(json.dumps(xmltodict.parse(response.text.encode('utf-8'))))
            detail = response["s:Envelope"]["s:Body"]["HotelDetailResponse"]["HotelDetailResult"]["HotelDetail"]

            db.vanila_hotel_list.update({'HotelId': hotelid}, {'$set': {'hoteldetail': detail}})
            # db.vanila_error.remove({'id': hotelid})
            print('ok')
        except:
            try:
                db.vanila_error2.insert({'hotelid': hotelid, 'response': response})
                # db.vanila_error.remove({'id': hotelid})
            except:
                print(traceback.format_exc())
            print('err')

    def add_hotel_detail(self):
        hotel_ids = list(db.vanila_hotel_list.find({'hoteldetail': {'$eq': None}}, {'HotelId': 1, '_id': 0}))
        hotel_ids = [item["HotelId"] for item in hotel_ids]

        for id in hotel_ids:
            self.get_hotel_details(id)
            time.sleep(0.5)

    def find_hotel_from_collection(self):
        return db.vanila_hotel_list.find_one({'mark': None})

    def get_giata_code(self, hotel_id):
        try:
            return db.vanila_giata.find_one({'HOTELID': hotel_id}, {'_id': 0})['GiataId']
        except:
            return None

    def set_facility_value(self, hotel, hotel_info):
        hotel_facility = hotel['hoteldetail']['HotelFacilityIds']['int']
        hotel_facility = [self.dictionary['schema_m1']['dict_hotel_facilities'][item] for item in hotel_facility if item != '0'] if hotel_facility == '0' else []

        room_facility = hotel['hoteldetail']['RoomFacilityIds']['int']
        room_facility = [self.dictionary['schema_m1']['dict_room_facilities'][item] for item in room_facility if item != '0'] if room_facility == '0' else []

        total_basis_facilities = {}
        for fixed_item in self.dictionary['schema_m1']['fixed_list']:
            for title, options in fixed_item.items():
                common_hotel_facility = list(set(hotel_facility).intersection(options)) if len(hotel_facility) != 0 else hotel_facility
                common_room_facility = list(set(room_facility).intersection(options)) if len(room_facility) != 0 else room_facility

                if len(common_hotel_facility) != 0:
                    total_basis_facilities = set(total_basis_facilities) | set(common_hotel_facility)
                    hotel_info[title] = common_hotel_facility

                if len(common_room_facility) != 0:
                    total_basis_facilities = set(total_basis_facilities) | set(common_room_facility)
                    hotel_info[title] = common_room_facility
        total_vanila_facility = (set(room_facility) | set(hotel_facility))
        total_vanila_facility = {} if len(total_vanila_facility) == 0 else total_vanila_facility
        remaining = set(total_vanila_facility) - set(total_basis_facilities)
        self.remaining_facility.extend(remaining)
        return hotel_info

    def set_field_value_to_basis_title(self, hotel):
        self.giata_code = self.get_giata_code(hotel['HotelId'])
        if self.giata_code:
            hotel_info = {}
            for key, value in self.dictionary['schema_m1']['dict_hotel_field'].items():
                field_value = validation(key, eval(value['path']), value['typeid'])
                if not (field_value) and value['optional'] == 0:
                    logger.info(f'****deleted_hotel for vanila****:{hotel}')
                    return None
                elif field_value and field_value != 'null':
                    hotel_info[key] = field_value
            return hotel_info
        else:
            return None

    def set_status(self, msg):
        if msg == 'error':
            db.vanila_hotel_list.update({'HotelId': self.hotel_id}, {'$unset': {'mark': ''}})
        client.close()

    def hotel_data_integration(self):
        self.update_hotels()
        print('*undating hotels is completed*')
        self.add_hotel_detail()
        print('*adding hotel detail is completed*')

    def finding_usedforid(self, giata_code):
        used_for_id = db.giata_with_basis_id.find_one({'giata': giata_code})['basis_id']
        method = 'update'
        if used_for_id == 0:
            used_for_id = usedforId_producer.produce_usedforid()
            print('~~~~~~~~~~~~~~used_for_id:', used_for_id)
            db.giata_with_basis_id.update({"giata": self.giata_code}, {'$set': {'basis_id': int(used_for_id)}})
            # used_for_id = 'mehrrrrrrr'
            method = 'insert'
        return used_for_id, method

    def marking_hotels(self, id):
        db.vanila_hotel_list.update({'HotelId': id}, {'$set': {'mark': 1}})

    def insert_image(self, used_for_id, hotel):
        try:
            photos = hotel['hoteldetail']['HotelPhotos']['string']
            finded_service_image = list(db.webserviceimage.find({'basis_id': used_for_id}))
            if finded_service_image:
                exsiting_photos = finded_service_image[0]['photo']
                total_photos = list(set(exsiting_photos + photos))
                db.webserviceimage.update({'basis_id': used_for_id}, {'$set': {'photo': total_photos}})
            else:
                db.webserviceimage.insert({'basis_id': used_for_id, 'photo': photos})
        except:
            pass

    def export_data(self):
        result = {}
        hotel = self.find_hotel_from_collection()
        self.hotel_id = hotel['HotelId']
        temp_result = self.set_field_value_to_basis_title(hotel)
        if temp_result:
            used_for_id, method = self.finding_usedforid(self.giata_code)
            temp_result = self.set_facility_value(hotel, temp_result)
            temp_result.update({'city': self.get_city_info(hotel['CityId']), 'country': self.get_country_info(hotel['CountryId']), 'usedForID': used_for_id, 'method': method})
            result.update(temp_result)
            self.insert_image(used_for_id, hotel)
        facility_logger.info(f'the facilities do not exist in basisCore: {set(self.remaining_facility)}')
        self.marking_hotels(hotel['HotelId'])

        return result
