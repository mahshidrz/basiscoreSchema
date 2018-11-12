from bson import ObjectId
import json


class Basis(object):
    def __init__(self, SchemaID, Lid, DmnID):  # chizaye base k domain mikhad bahash kar kone
        self.Lid = Lid
        self.SchemaID = SchemaID
        self.DmnID = DmnID


class Core(Basis):
    def __init__(self, name, usedforid, group, SchemaID, Lid, DmnID):
        super().__init__(SchemaID, Lid, DmnID)

        # attribute hayi k tamame schema ha darand:
        self.name = name
        self.usedforid = usedforid
        self.Group = group
        self.Cat = []
        self.imageurl_small = ''
        self.imageurl_med = ''
        self.imageurl_large = ''


class schema(Core):
    def __init__(self, name, usedforid, group, SchemaID, Lid, DmnID):
        super().__init__(name, usedforid, group, SchemaID, Lid, DmnID)
        with open('schema.j') as f:
            self.data = json.load(f)

    def get_properties(self, providerID):
        providers = {
            "0": "Namayeshgah",
            "0.0": "Namayeshgah",
            "9.0": "Dreamdays",
            "9": "Dreamdays",
            "10.0": "Vanila",
            "10": "Vanila",
            "23": "Seatravel",
            "23.0": "Seatravel",
            "11": "Parsian",
            "11.0": "Parsian"
        }
        provider_data = eval(providers[providerID] + '()')
        return provider_data

    def return_data(self):
        result = {}
        provider_data = self.get_properties(self.providerID)
        hotel_collection = {
            "_id": ObjectId("5ba9fc558b9f893966b68e8e"),
            "Address": "Scanderbeg Square, Build. 8 , Entr. 1street Tirana",
            "Category": 4,
            "CityId": 8,
            "CountryId": 6,
            "Email": "HOTEL@HOTELTIRANA.COM.AL",
            "Fax": " 355 42 234188",
            "HotelId": 1807973,
            "LastUpdateDate": "/Date(1435559006443+0300)/",
            "Lat": 41.329645,
            "Lon": 19.818595,
            "Phone": " 355 42 234185",
            "Zipcode": "",
            "hoteldetail": {
                "HotelId": "1807973",
                "HotelName": "Tirana International Hotel Conference Centre",
                "HotelAddress": "Scanderbeg Square, Build. 8 , Entr. 1street Tirana",
                "HotelChainId": "0",
                "CountryId": "6",
                "CityId": "8",
                "CategoryId": "4",
                "Latitude": "41.329645",
                "Longitude": "19.818595",
                "HotelFacilityIds": {
                    "int": [
                        "78",
                        "842",
                        "334",
                        "842",
                        "36",
                        "10616",
                        "165",
                        "54",
                        "343",
                        "49",
                        "4",
                        "78",
                        "58",
                        "261",
                        "313",
                        "20",
                        "890",
                        "335",
                        "15",
                        "10616",
                        "115"
                    ]
                },
                "RoomFacilityIds": {
                    "int": [
                        "6",
                        "16",
                        "17",
                        "7",
                        "8",
                        "9",
                        "10",
                        "11",
                        "18",
                        "26",
                        "14",
                        "32",
                        "19",
                        "31",
                        "20",
                        "15",
                        "21",
                        "22",
                        "23",
                        "24",
                        "2",
                        "4",
                        "797"
                    ]
                },
                "ChildAgeMin": "0",
                "ChildAgeMax": "0",
                "ConstructedYear": "0",
                "RenovatedYear": "0",
                "TotalRooms": "0",
                "TotalFloors": "0",
                "HotelDesc": "Tirana International Hotel & Conference Centre is one of the most prestigious and largest hotels in Albania on Scanderbeg Square. Tirana International Hotel has always been considered the symbol of the capital. Built during Albania’s isolation years with an imposing socialist architectural style, Tirana International Hotel used to be the tallest building in the country. Furthermore Tirana International Hotel was exclusively used for foreign delegations and tourists, making it intriguing and mysterious for Albanians. In 2001Tirana International Hotel was totally renovated to a four star hotel of international standards by an Italian firm, while still retaining its grandiose past features. Tirana International Hotel has been for years the place for important events in Albania and home to many international business travelers who appreciate Excellence in Service. Since the arrival at the Tirana International Hotel, the cheerful attitude of the employees dedicated to achieve total customer satisfaction make the stay at the Tirana International Hotel an enjoyable experience.",
                "Location": "The hotel is located in Tirana, Albania. It is situated in the commercial centre of the city and is surrounded by shops, bars and restaurants. The hotel is 35 km from the beach and the port of Durres, and Tirana Airport is just 28 km away. The opera house, palace and central bank are located just across the square.",
                "Area": "Airport: Tirana Rinas from K 13.0",
                "Lobby": None,
                "Room": "All of the en suite rooms include a hairdryer, direct dial telephone, minibar, cable TV, radio, safe, plus heating and air conditioning units. All the rooms feature either a double or king-size bed.",
                "Restaurant": None,
                "Exterior": None,
                "HotelPhotos": {
                    "string": [
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/11.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/12.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/13.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/14.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/15.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/16.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/17.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/18.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/19.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/20.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/21.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/22.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/23.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/24.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/25.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/26.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/27.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/28.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/29.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/30.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/31.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/32.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/33.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/34.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/35.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/36.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/37.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/38.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/39.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/40.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/41.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/42.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/43.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/44.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/45.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/46.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/47.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/48.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/49.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/50.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/51.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/52.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/53.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/54.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/55.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/56.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/57.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/58.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/59.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/60.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/61.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/62.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/63.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/64.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/65.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/66.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/67.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/68.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/69.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/70.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/71.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/72.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/73.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/74.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/75.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/76.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/77.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/78.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/79.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/80.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/81.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/82.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/83.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/84.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/85.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/86.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/87.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/88.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/89.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/90.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/91.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/92.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/93.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/94.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/95.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/96.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/97.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/98.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/99.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/100.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/101.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/102.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/103.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/104.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/105.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/106.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/107.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/108.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/109.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/110.jpg",
                        "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/111.jpg"
                    ]
                },
                "RequestIp": "84.241.22.93"
            },
            "giata": {
                "HOTELID": 1807973
            },
            "Hotel Name": "Tirana International Hotel Conference Centre",
            "Minimum check-in age is": "0",
            "GIATA": 87098,
            "Original Photo": [
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/11.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/12.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/13.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/14.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/15.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/16.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/17.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/18.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/19.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/20.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/21.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/22.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/23.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/24.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/25.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/26.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/27.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/28.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/29.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/30.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/31.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/32.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/33.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/34.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/35.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/36.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/37.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/38.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/39.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/40.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/41.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/42.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/43.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/44.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/45.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/46.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/47.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/48.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/49.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/50.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/51.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/52.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/53.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/54.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/55.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/56.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/57.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/58.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/59.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/60.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/61.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/62.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/63.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/64.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/65.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/66.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/67.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/68.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/69.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/70.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/71.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/72.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/73.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/74.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/75.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/76.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/77.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/78.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/79.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/80.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/81.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/82.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/83.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/84.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/85.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/86.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/87.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/88.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/89.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/90.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/91.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/92.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/93.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/94.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/95.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/96.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/97.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/98.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/99.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/100.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/101.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/102.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/103.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/104.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/105.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/106.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/107.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/108.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/109.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/110.jpg",
                "https://i.vanillatours.com/3/7/9/7/0/8/1/1807973/Y/111.jpg"
            ]
        }
        # print(self.data)
        for item in self.data:
            try:
                setattr(self, item['Title'], hotel_collection[item['Title']])
                result.update({item['Title']: hotel_collection[item['Title']]})
                # print(result)
            except:
                result.update({item['Title']: None})

        print('_schema length: ', len(self.data))
        print('result length: ', len(result))
        print('hotel_collection length: ', len(hotel_collection))
        print(result)
        return result


schema('hotel', 0, [], 251, 2, 2452).return_data()
