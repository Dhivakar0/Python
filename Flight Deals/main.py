#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

flight_search = FlightSearch()

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

# sheet_data = [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
#  {'city': 'Frankfurt', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
#  {'city': 'Austin', 'iataCode': '', 'id': 4, 'lowestPrice': 485}]

for city in sheet_data:
    if city['iataCode'] == "":
        city['iataCode'] = flight_search.get_destination_code(city['city'])

data_manager.destination_data = sheet_data
data_manager.update_destination_data()


