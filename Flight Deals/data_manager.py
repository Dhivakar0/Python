import requests
# from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

sheety_api_endpoint = "https://api.sheety.co/1be0483e92ce611e6b5943d8a8f58ca7/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.api_key = os.environ["API_KEY"]
        self.headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_api_endpoint,headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city_name in self.destination_data:
            new_data = {
                'price':
                    {
                        'iataCode' : city_name['iataCode']
                    }
            }

            requests.put(url=f"{sheety_api_endpoint}/{city_name['id']}",
                                    json=new_data,
                                    headers=self.headers)





