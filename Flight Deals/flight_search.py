import os
from dotenv import load_dotenv
import requests

load_dotenv()

access_token_server = "https://test.api.amadeus.com/v1/security/oauth2/token"
city_api_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
flight_offers_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.key = os.environ["AMADEUS_API_KEY"]
        self.secret = os.environ["AMADEUS_API_SECRET"]
        self.token = self.get_token()

    def get_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.key,
            'client_secret': self.secret
        }
        response = requests.post(url=access_token_server,headers=header,data=body)
        self.token = response.json()['access_token']
        return self.token


    def get_destination_code(self,city):
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            'keyword': city,
            'max' : '2',
            'include' : "AIRPORTS"
        }
        response = requests.get(url=city_api_endpoint,headers=headers,params=query)

        print(f"status code {response.status_code}. Airport IATA: {response.text}")

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No Airport codes found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code

    def check_flights(self,origin_city_code,destination_city_code,from_time,to_time):
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            'originLocationCode': origin_city_code,
            'destinationLocationCode': destination_city_code,
            'departureDate': from_time.strftime("%Y-%m-%d"),
            'returnDate' : to_time.strftime("%Y-%m-%d"),
            'adults': '1',
            "nonStop": "true",
            "currencyCode": "GBP",
            'max': '20'
        }
        response = requests.get(url=flight_offers_endpoint,params=query,headers=headers)

        if response.status_code != 200:
            print(f"check_flights() response code:{response.status_code}")
            print(f"Response:{response.text}")
            return None

        return response.json()

