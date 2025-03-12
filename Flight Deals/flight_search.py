import requests

# amadeus_api_endpoint = "https://test.api.amadeus.com/v1/shopping/flight-dates"
# amadeus_api_key = "xrXnq0kIjDgMWGQ0tnVtkO7fDIZJVHZA"
# amadeus_api_secret = "bR9966ToSD9s35Ts"
#
# access_token_server = "https://test.api.amadeus.com/v1/security/oauth2/token"
#
# access_token = 'GmYotXVyZRPPlhmDwRynGDTQuZKH'
#
# # Define the headers
# # amadeus_headers = {
# #     'Content-Type': 'application/x-www-form-urlencoded'
# # }
# #
# # # Define the data (form parameters)
# # data = {
# #     'grant_type': 'client_credentials',
# #     'client_id': amadeus_api_key,
# #     'client_secret': amadeus_api_secret
# # }
# #
# # response = requests.post(url=access_token_server,headers=amadeus_headers,data=data)
# #
# # if response.status_code == 200:
# #     token = response.json()
# #     print(token)
# # else:
# #     print(f"Error:{response.status_code}")
# #     print(response.text)
#
# flight_api_endpoint = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
#
# headers = {
#     'Authorization': f'Bearer {access_token}'
# }
# params = {
#     'origin': 'PAR',  # Origin airport code (paris)
#     'maxPrice': 200   # Maximum price
# }
#
# response = requests.get(url=flight_api_endpoint,headers=headers,params=params)
#
# if response.status_code == 200:
#     # Parse and print the response JSON
#     data = response.json()
#     print("Response Data:", data)
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self,city):
        code = "Testing"
        return code

# Response Data: {'data': [{'type': 'flight-destination', 'origin': 'ORY', 'destination': 'MAD', 'departureDate': '2025-03-25', 'returnDate': '2025-03-26', 'price': {'total': '112.68'}, 'links': {'flightDates': 'https://test.api.amadeus.com/v1/shopping/flight-dates?origin=PAR&destination=MAD&departureDate=2025-03-13,2025-09-08&oneWay=false&duration=1,15&nonStop=false&maxPrice=200&currency=EUR&viewBy=DURATION', 'flightOffers': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=PAR&destinationLocationCode=MAD&departureDate=2025-03-25&returnDate=2025-03-26&adults=1&nonStop=false&maxPrice=200&currency=EUR'}}, {'type': 'flight-destination', 'origin': 'ORY', 'destination': 'OPO', 'departureDate': '2025-05-13', 'returnDate': '2025-05-21', 'price': {'total': '123.41'}, 'links': {'flightDates': 'https://test.api.amadeus.com/v1/shopping/flight-dates?origin=PAR&destination=OPO&departureDate=2025-03-13,2025-09-08&oneWay=false&duration=1,15&nonStop=false&maxPrice=200&currency=EUR&viewBy=DURATION', 'flightOffers': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=PAR&destinationLocationCode=OPO&departureDate=2025-05-13&returnDate=2025-05-21&adults=1&nonStop=false&maxPrice=200&currency=EUR'}}, {'type': 'flight-destination', 'origin': 'ORY', 'destination': 'LIS', 'departureDate': '2025-06-24', 'returnDate': '2025-07-01', 'price': {'total': '130.53'}, 'links': {'flightDates': 'https://test.api.amadeus.com/v1/shopping/flight-dates?origin=PAR&destination=LIS&departureDate=2025-03-13,2025-09-08&oneWay=false&duration=1,15&nonStop=false&maxPrice=200&currency=EUR&viewBy=DURATION', 'flightOffers': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=PAR&destinationLocationCode=LIS&departureDate=2025-06-24&returnDate=2025-07-01&adults=1&nonStop=false&maxPrice=200&currency=EUR'}}, {'type': 'flight-destination', 'origin': 'ORY', 'destination': 'LIN', 'departureDate': '2025-03-14', 'returnDate': '2025-03-16', 'price': {'total': '135.45'}, 'links': {'flightDates': 'https://test.api.amadeus.com/v1/shopping/flight-dates?origin=PAR&destination=LIN&departureDate=2025-03-13,2025-09-08&oneWay=false&duration=1,15&nonStop=false&maxPrice=200&currency=EUR&viewBy=DURATION', 'flightOffers': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=PAR&destinationLocationCode=LIN&departureDate=2025-03-14&returnDate=2025-03-16&adults=1&nonStop=false&maxPrice=200&currency=EUR'}}, {'type': 'flight-destination', 'origin': 'CDG', 'destination': 'FCO', 'departureDate': '2025-03-19', 'returnDate': '2025-04-01', 'price': {'total': '150.05'}, 'links': {'flightDates': 'https://test.api.amadeus.com/v1/shopping/flight-dates?origin=PAR&destination=FCO&departureDate=2025-03-13,2025-09-08&oneWay=false&duration=1,15&nonStop=false&maxPrice=200&currency=EUR&viewBy=DURATION', 'flightOffers': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=PAR&destinationLocationCode=FCO&departureDate=2025-03-19&returnDate=2025-04-01&adults=1&nonStop=false&maxPrice=200&currency=EUR'}}, {'type': 'flight-destination', 'origin': 'ORY', 'destination': 'BCN', 'departureDate': '2025-03-30', 'returnDate': '2025-04-01', 'price': {'total': '152.76'}, 'links': {'flightDates': 'https://test.api.amadeus.com/v1/shopping/flight-dates?origin=PAR&destination=BCN&departureDate=2025-03-13,2025-09-08&oneWay=false&duration=1,15&nonStop=false&maxPrice=200&currency=EUR&viewBy=DURATION', 'flightOffers': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=PAR&destinationLocationCode=BCN&departureDate=2025-03-30&returnDate=2025-04-01&adults=1&nonStop=false&maxPrice=200&currency=EUR'}}, {'type': 'flight-destination', 'origin': 'ORY', 'destination': 'TUN', 'departureDate': '2025-03-16', 'returnDate': '2025-03-20', 'price': {'total': '155.83'}, 'links': {'flightDates': 'https://test.api.amadeus.com/v1/shopping/flight-dates?origin=PAR&destination=TUN&departureDate=2025-03-13,2025-09-08&oneWay=false&duration=1,15&nonStop=false&maxPrice=200&currency=EUR&viewBy=DURATION', 'flightOffers': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=PAR&destinationLocationCode=TUN&departureDate=2025-03-16&returnDate=2025-03-20&adults=1&nonStop=false&maxPrice=200&currency=EUR'}}, {'type': 'flight-destination', 'origin': 'ORY', 'destination': 'RAK', 'departureDate': '2025-09-02', 'returnDate': '2025-09-17', 'price': {'total': '157.96'}, 'links': {'flightDates': 'https://test.api.amadeus.com/v1/shopping/flight-dates?origin=PAR&destination=RAK&departureDate=2025-03-13,2025-09-08&oneWay=false&duration=1,15&nonStop=false&maxPrice=200&currency=EUR&viewBy=DURATION', 'flightOffers': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=PAR&destinationLocationCode=RAK&departureDate=2025-09-02&returnDate=2025-09-17&adults=1&nonStop=false&maxPrice=200&currency=EUR'}}, {'type': 'flight-destination', 'origin': 'CDG', 'destination': 'ATH', 'departureDate': '2025-06-17', 'returnDate': '2025-06-30', 'price': {'total': '165.73'}, 'links': {'flightDates': 'https://test.api.amadeus.com/v1/shopping/flight-dates?origin=PAR&destination=ATH&departureDate=2025-03-13,2025-09-08&oneWay=false&duration=1,15&nonStop=false&maxPrice=200&currency=EUR&viewBy=DURATION', 'flightOffers': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=PAR&destinationLocationCode=ATH&departureDate=2025-06-17&returnDate=2025-06-30&adults=1&nonStop=false&maxPrice=200&currency=EUR'}}], 'dictionaries': {'currencies': {'EUR': 'EURO'}, 'locations': {'LIN': {'subType': 'AIRPORT', 'detailedName': 'LINATE'}, 'MAD': {'subType': 'AIRPORT', 'detailedName': 'ADOLFO SUAREZ BARAJAS'}, 'FCO': {'subType': 'AIRPORT', 'detailedName': 'FIUMICINO'}, 'ATH': {'subType': 'AIRPORT', 'detailedName': 'ATHENS INT E VENIZELOS'}, 'ORY': {'subType': 'AIRPORT', 'detailedName': 'ORLY'}, 'LIS': {'subType': 'AIRPORT', 'detailedName': 'AIRPORT'}, 'CDG': {'subType': 'AIRPORT', 'detailedName': 'CHARLES DE GAULLE'}, 'TUN': {'subType': 'AIRPORT', 'detailedName': 'CARTHAGE'}, 'BCN': {'subType': 'AIRPORT', 'detailedName': 'JOSEP TARRADELLAS BARCELONA'}, 'RAK': {'subType': 'AIRPORT', 'detailedName': 'MENARA'}, 'OPO': {'subType': 'AIRPORT', 'detailedName': 'FRANCISCO SA CARNEIRO'}}}, 'meta': {'currency': 'EUR', 'links': {'self': 'https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=PAR&departureDate=2025-03-13,2025-09-08&oneWay=false&duration=1,15&nonStop=false&maxPrice=200&viewBy=DESTINATION'}, 'defaults': {'departureDate': '2025-03-13,2025-09-08', 'oneWay': False, 'duration': '1,15', 'nonStop': False, 'viewBy': 'DESTINATION'}}}
