import datetime
import time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_affordable_flight
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()
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

customer_emails = data_manager.get_customer_emails()

tomorrow_date = datetime.datetime.now() + datetime.timedelta(days=1)
six_months_from_today = datetime.datetime.now() + datetime.timedelta(days = (6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")

    flights = flight_search.check_flights(origin_city_iata,destination['iataCode'],from_time=tomorrow_date,to_time=six_months_from_today)

    affordable_flight = find_affordable_flight(flights)
    print(f"{destination['city']}: £{affordable_flight.price}")
    time.sleep(2)

    if affordable_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stop_over_flights = flight_search.check_flights(origin_city_iata, destination['iataCode'], from_time=tomorrow_date,
                                              to_time=six_months_from_today, is_direct=False)
        affordable_flight_with_stops = find_affordable_flight(stop_over_flights)
        print(f"Affordable indirect flight price is: £{affordable_flight_with_stops.price} ")

    if affordable_flight.price != "N/A" and affordable_flight.price < destination['lowestPrice']:
        if affordable_flight.stops == 0:
            message=f"Low price alert! Only £{affordable_flight.price} to fly "\
                         f"from {affordable_flight.origin} to {affordable_flight.destination}, "\
                         f"on {affordable_flight.departure_date} until {affordable_flight.return_date}."

        else:
            message=f"Low price alert! Only £{affordable_flight.price} to fly "\
                         f"from {affordable_flight.origin} to {affordable_flight.destination}, "\
                         f"with {affordable_flight.stops} stops "\
                         f"on {affordable_flight.departure_date} until {affordable_flight.return_date}."

        print(f"Check your email. Lower price flight found to {destination['city']}!")

        notification_manager.send_message(message_body=message)

        notification_manager.send_mails(email_list=customer_emails,message=message)




