from bson import ObjectId
import json
import copy
import pymssql
import requests
import collections
import xmltodict
from lxml import html
from vanila_data_integration_new import VanilaMappingProccess
from seatravel_data_integration import SeatravelMappingProccess


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

    def get_XML(self, lid, usedforID):
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
        return XML

    def get_dictionary_provider(self):
        url = "http://user.efeh.com/get-dictionary.bc"

        querystring = {"providerid": str(self.providerID)}

        payload = ""
        headers = {
            'User-Agent': 'python-requests/2.8.1',
            'Content-Type': 'text/html',
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        return response.text

    def get_properties(self):
        providers = {
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
        dictionary = self.get_dictionary_provider()
        provider_data = eval(providers[str(self.providerID)] + '(' + dictionary + ').' + 'export_data()')
        usedFor_ID = provider_data['usedForID']
        method = provider_data['method']
        org_xml = self.get_XML(2, usedFor_ID)
        if method == 'insert':
            result = self.XML_generator_insert(provider_data, org_xml)
        elif method == 'update':
            result = self.XML_generator_update(provider_data, org_xml)
        else:
            result = None
        return result

    def XML_generator_insert(self, dict_result, org_xml):
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
        out = xmltodict.unparse(dict_XML, pretty=True)
        print(out)

        return out

    def XML_generator_update(self, dict_result, org_xml):
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

        print(dict_XML)
        return self.providerID

    def insert_into_SQL(self):
        # xml = self.get_properties()
        xml = '''<root>
	<properties LID="2" MId="10" usedForId="1290136" script="" helpUrl="/PrpHelpUrl.aspx" submitClass="submit_xml" uiType="form" multi="false" submitImageUrl="/images/submit/submit.png" errorUrl="/xmlerror_print.json">
		<property question="Hotel Name" prpid="1360" multi="false">
			<answers>
				<answer valueId="0">
					<part v_minlength="2" v_maxlength="100" v_required="true" class="CSS_150" type="text" order="3">JA Hatta Fort Hotel</part>
				</answer>
			</answers>
		</property>
		<property question="star rating" prpid="1361" multi="false">
			<answers>
				<answer valueId="0">
					<part v_min="1" class="css_130" type="text" order="1" v_number="true">4</part>
				</answer>
			</answers>
		</property>
		<property question="facilities" prpid="1367" multi="false">
			<answers>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="2369"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="2213"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="2054"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="155815"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="2056"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="2216"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="155819"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="2061"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="2062"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="144206"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="2065"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="155826"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="2067"></part>
				</answer>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1367" value="2068"></part>
				</answer>
			</answers>
		</property>
		<property question="room facilities" prpid="1369" multi="false">
			<answers>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1369" value="155850"></part>
				</answer>
			</answers>
		</property>
		<property question="ventilation system" prpid="1372" multi="false">
			<answers>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1372" value="2096"></part>
				</answer>
			</answers>
		</property>
		<property question="country" prpid="10000005" multi="false">
			<answers>
				<answer valueId="0">
					<part type="textList" order="3" class="CSS_199" url="/jsonsearch/jsonsearch.htm?mid2=10&amp;Prpid=10000005&amp;lid=2" text="United Arab Emirates" value="1002248"></part>
				</answer>
			</answers>
		</property>
		<property question="city" prpid="10000006" multi="false">
			<answers>
				<answer valueId="0">
					<part type="textList" order="3" class="CSS_199" url="/jsonsearch/jsonsearch.htm?mid2=10&amp;Prpid=10000006&amp;lid=2" text="Hatta" value="1176288"></part>
				</answer>
			</answers>
		</property>
		<property question="parking" prpid="2651" multi="false">
			<answers>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=2651" value="2193"></part>
				</answer>
			</answers>
		</property>
		<property question="sport and entertainment" prpid="1374" multi="false">
			<answers>
				<answer valueId="0">
					<part class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=1374" value="2207"></part>
				</answer>
			</answers>
		</property>
		<property question="shuttle" prpid="2671" multi="false">
			<answers>
				<answer valueId="0">
					<part v_minlength="2" v_maxlength="4000" class="CSS_140" type="checkList" order="3" url="/PrpfixUrl.aspx?Lid=2&amp;Prpid=2671" value="2243"></part>
				</answer>
			</answers>
		</property>
		<property question="Address" prpid="1379" multi="false">
			<answers>
				<answer valueId="0">
					<part class="css_244" type="largeText" order="3">Dubai-Hatta Road/P.O. Box 9277/Hatta</part>
				</answer>
			</answers>
		</property>
		<property question="Phone" prpid="1380" multi="true">
			<answers>
				<answer valueId="0">
					<part v_minlength="2" v_maxlength="4000" class="css_241" type="text" order="3">+97148099333</part>
				</answer>
			</answers>
		</property>
		<property question="Fax" prpid="1381" multi="false">
			<answers>
				<answer valueId="0">
					<part v_minlength="2" v_maxlength="4000" class="css_241" type="text" order="3">+97148523561</part>
				</answer>
			</answers>
		</property>
		<property question="Website" prpid="1382" multi="false">
			<answers>
				<answer valueId="0">
					<part v_minlength="2" v_maxlength="4000" class="CSS_250" type="text" order="3">https://www.jaresortshotels.com/propertyoverview/dubai/ja-hatta-fort-hotel</part>
				</answer>
			</answers>
		</property>
		<property question="GIATA" prpid="73547" multi="false">
			<answers>
				<answer valueId="0">
					<part v_min="1" class="css_130" type="text" order="1" v_number="true">13829</part>
				</answer>
			</answers>
		</property>
	</properties>
</root>
'''
        url = "http://172.20.19.46/test_jafarzadeh2.bc"
        payload = {"xmldata": xml}

        response = requests.post(url, payload)
        # print(response.text)
        return response.text

        pass


Schema(251, 2, 2452)
print(Fetch(23, 251, 2, 2452).get_properties())
