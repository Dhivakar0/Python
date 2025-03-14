#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime
import time

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_affordable_flight


flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)
origin_city_iata = 'LON'

for city_name in sheet_data:
    if city_name['iataCode'] == "":
        city_name['iataCode'] = flight_search.get_destination_code(city_name['city'])
        time.sleep(2)
# print(f"sheet data:\n{sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_data()

tomorrow_date = datetime.datetime.now() + datetime.timedelta(days=1)
six_months_from_today = datetime.datetime.now() + datetime.timedelta(days = (6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(origin_city_iata,destination['iataCode'],from_time=tomorrow_date,to_time=six_months_from_today)

    affordable_flight = find_affordable_flight(flights)
    print(f"{destination['city']}: £{affordable_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

# ********//////////////////////////

# [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54},
#  {'city': 'Frankfurt', 'iataCode': 'FRA', 'id': 3, 'lowestPrice': 42},
#  {'city': 'Austin', 'iataCode': 'ASQ', 'id': 4, 'lowestPrice': 485}]
