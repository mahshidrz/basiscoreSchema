from bson import ObjectId
import time
import sys
import ast
import copy
import pymssql
import requests
import collections
import xmltodict
from lxml import html
from hotels.vanila_data_integration_new import VanilaMappingProccess
from hotels.seatravel_data_integration import SeatravelMappingProccess


class Basis(object):
    def __init__(self, SchemaID, Lid, DmnID):  # chizaye base k domain mikhad bahash kar kone
        self.Lid = Lid
        self.SchemaID = SchemaID
        self.DmnID = DmnID


class Core(Basis):
    def __init__(self, usedforid, SchemaID, Lid, DmnID):
        super().__init__(SchemaID, Lid, DmnID)

        # attribute hayi k tamame schema ha darand:
        # self.name = name
        # self.Group = group
        self.Cat = []
        self.imageurl_small = ''
        self.imageurl_med = ''
        self.imageurl_large = ''


class Schema:
    def __init__(self, SchemaID, Lid, DmnID):
        # super()
        self.Lid = Lid
        self.SchemaID = SchemaID

    def get_schema(self):
        url = "http://user.efeh.com/get-schema.bc"
        querystring = {"schemaid": str(self.SchemaID), "lid": str(self.Lid)}

        payload = ""
        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        # print(response.text)
        return response.text


class Fetch(Schema):
    def __init__(self, providerID, SchemaID, Lid, DmnID):
        super().__init__(SchemaID, Lid, DmnID)
        self.providerID = providerID
        self.providers = {
            "0": "Namayeshgah",
            "0.0": "Namayeshgah",
            "9.0": "Dreamdays",
            "9": "Dreamdays",
            "10.0": "VanilaMappingProccess",
            "10": "VanilaMappingProccess",
            "23": "SeatravelMappingProccess",
            "23.0": "SeatravelMappingProccess",
            "11": "Parsian",
            "11.0": "Parsian"
        }
        self.dictionary = self.get_dictionary_provider()
        self.provider_obj = eval(self.providers[str(self.providerID)] + '(' + self.dictionary + ')')

    def get_XML(self, lid, usedforID):
        start_time = time.time()
        db = pymssql.connect(server='172.20.19.46', user='sa', password='Salam1Salam2', database='exhibitor')
        cursor = db.cursor()
        cursor.execute('''declare @xml nvarchar(max)
                EXECUTE  [dbo].[xmlGenerateDBsource]
                {},
                {},
                {},
                @xml out,
                {},
                {},
                {}

             select @xml'''.format(10, usedforID, lid, 0, 0, 0))

        XML = cursor.fetchall()
        cursor.close()
        db.close()
        for i in XML:
            XML = i[0]
        print("--- get_XML %s seconds ---" % (time.time() - start_time))
        return XML

    def get_dictionary_provider(self):
        start_time = time.time()
        url = "http://user.efeh.com/get-dictionary.bc"

        querystring = {"providerid": str(self.providerID)}

        payload = ""
        headers = {
            'User-Agent': 'python-requests/2.8.1',
            'Content-Type': 'text/html',
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        print("--- get_dictionary_provider %s seconds ---" % (time.time() - start_time))
        return response.text

    def provider_data(self):
        start_time = time.time()
        provider_data = self.provider_obj.export_data()
        # print(provider_data)
        usedFor_ID = provider_data['usedForID']
        method = provider_data['method']
        org_xml = self.get_XML(2, usedFor_ID)
        if method == 'insert':
            result = self.XML_generator_insert(provider_data, org_xml)
        elif method == 'update':
            result = self.XML_generator_update(provider_data, org_xml)
        else:
            result = None
        print("--- provider_data %s seconds ---" % (time.time() - start_time))
        return result

    def XML_generator_insert(self, dict_result, org_xml):
        start_time = time.time()
        dict_xml = xmltodict.parse(org_xml, process_namespaces=True)
        dict_XML = collections.OrderedDict(dict_xml)

        field_name_list = [item for item in dict_result]
        removed_property_index = []

        for root, properties_list in dict_XML.items():
            for property_index in range(0, len(properties_list['properties']['property'])):
                for key, value in dict_result.items():
                    if key == properties_list['properties']['property'][property_index]['@question'] and type(value) is not list and type(value) is not dict and type(
                            value) is not tuple:
                        properties_list['properties']['property'][property_index]['answers']['answer']['part']['#text'] = str(value)
                    if key == properties_list['properties']['property'][property_index]['@question'] and type(value) is list:
                        new_answer = []
                        for i in value:
                            answer = properties_list['properties']['property'][property_index]['answers']['answer']
                            ans = copy.deepcopy(answer)
                            ans['part']['@value'] = str(int(i))
                            new_answer.append(ans)

                        properties_list['properties']['property'][property_index]['answers']['answer'] = new_answer
                    if key == properties_list['properties']['property'][property_index]['@question'] and type(value) is dict:
                        properties_list['properties']['property'][property_index]['answers']['answer']['part']['@text'] = value['title']
                        properties_list['properties']['property'][property_index]['answers']['answer']['part']['@value'] = str(int(value['id']))

                    if key == properties_list['properties']['property'][property_index]['@question'] and type(value) is tuple:
                        properties_list['properties']['property'][property_index]['answers']['answer']['part'][0]['#text'] = str(value[0])
                        properties_list['properties']['property'][property_index]['answers']['answer']['part'][1]['#text'] = str(value[1])

                if properties_list['properties']['property'][property_index]['@question'] not in field_name_list:
                    removed_property_index.append(property_index)

        dict_XML['root']['properties']['property'] = [item for index, item in enumerate(dict_XML['root']['properties']['property']) if index not in removed_property_index]

        # print(dict_XML)
        insert_out = xmltodict.unparse(dict_XML, full_document=False, pretty=True)
        print("--- XML_generator_insert %s seconds ---" % (time.time() - start_time))
        return insert_out

    def XML_generator_update(self, dict_result, org_xml):
        start_time = time.time()
        dict_xml = xmltodict.parse(org_xml, process_namespaces=True)
        dict_XML = collections.OrderedDict(dict_xml)
        null_question = []
        field_name_list = [item for item in dict_result]
        removed_property_index = []
        for K, properties_list in dict_XML.items():
            for x in range(0, len(properties_list['properties']['property'])):
                if type(properties_list['properties']['property'][x]['answers']['answer']) == list:
                    for i in properties_list['properties']['property'][x]['answers']['answer']:
                        if i['@valueId'] != '0':
                            null_question.append(x)
                else:
                    if properties_list['properties']['property'][x]['answers']['answer']['@valueId'] != '0':
                        null_question.append(x)

        dict_XML['root']['properties']['property'] = [item for index, item in enumerate(dict_XML['root']['properties']['property']) if index not in null_question]

        for root, properties_list in dict_XML.items():
            for property_index in range(0, len(properties_list['properties']['property'])):
                for key, value in dict_result.items():
                    if key == properties_list['properties']['property'][property_index]['@question'] and type(value) is not list and type(value) is not dict and type(
                            value) is not tuple:
                        properties_list['properties']['property'][property_index]['answers']['answer']['part']['#text'] = str(value)
                    if key == properties_list['properties']['property'][property_index]['@question'] and type(value) is list:
                        new_answer = []
                        for i in value:
                            answer = properties_list['properties']['property'][property_index]['answers']['answer']
                            ans = copy.deepcopy(answer)
                            ans['part']['@value'] = str(int(i))
                            new_answer.append(ans)

                        properties_list['properties']['property'][property_index]['answers']['answer'] = new_answer
                    if key == properties_list['properties']['property'][property_index]['@question'] and type(value) is dict:
                        properties_list['properties']['property'][property_index]['answers']['answer']['part']['@text'] = value['title']
                        properties_list['properties']['property'][property_index]['answers']['answer']['part']['@value'] = str(int(value['id']))

                    if key == properties_list['properties']['property'][property_index]['@question'] and type(value) is tuple:
                        properties_list['properties']['property'][property_index]['answers']['answer']['part'][0]['#text'] = str(value[0])
                        properties_list['properties']['property'][property_index]['answers']['answer']['part'][1]['#text'] = str(value[1])

                if properties_list['properties']['property'][property_index]['@question'] not in field_name_list:
                    removed_property_index.append(property_index)

        dict_XML['root']['properties']['property'] = [item for index, item in enumerate(dict_XML['root']['properties']['property']) if index not in removed_property_index]

        update_out = xmltodict.unparse(dict_XML, full_document=False, pretty=True)
        print("--- XML_generator_update %s seconds ---" % (time.time() - start_time))
        return update_out

    def insert_into_SQL(self):
        # try:
        start_time = time.time()
        XML = []
        for i in range(0, 10):
            xml = self.provider_data()
            XML.append(xml)
        for xml in XML:
            url = "http://172.20.19.46/test_jafarzadeh2.bc"
            payload = {"xmldata": xml}

            response = (requests.post(url, payload)).text
            try:
                ast.literal_eval(response)
                self.provider_obj.set_status('ok')
            except:
                self.provider_obj.set_status('error')

            print("--- insert_into_SQL %s seconds ---" % (time.time() - start_time))
            return response
        # except Exception as e:
        #     print(sys.stderr, "does not exist")
        #     print(sys.stderr, "Exception: %s" % str(e))
        #     sys.exit(1)


Schema(251, 2, 2452)
print(Fetch(10, 251, 2, 2452).insert_into_SQL())
