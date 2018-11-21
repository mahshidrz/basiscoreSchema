import time
from json import loads
from pymongo import MongoClient
import requests
import traceback


def info_seatravel():
    client = MongoClient('localhost', 27017)
    db = client.ticketlist

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
                print("/-------------------------ok save--->id: " + i + " ---------------------------/")
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


print(info_seatravel())
