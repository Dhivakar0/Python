import requests
from dotenv import load_dotenv
import os

load_dotenv()

sheety_api_endpoint = "https://api.sheety.co/1be0483e92ce611e6b5943d8a8f58ca7/flightDeals/prices"

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.api_key = os.environ["API_KEY"]
        self.headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        self.destination_data = {}

    def get_destination_data(self):
        try:
            # Make the GET request to the Sheety API
            response = requests.get(url=sheety_api_endpoint, headers=self.headers)

            # Check if the response is successful (status code 200)
            if response.status_code == 200:
                data = response.json()

                # Ensure the 'prices' key exists in the response
                if "prices" in data:
                    self.destination_data = data["prices"]
                    return self.destination_data
                else:
                    print("Error: 'prices' key not found in the response.")
                    return None
            else:
                print(f"Error: Unable to fetch data. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            # Catch any other errors (e.g., network issues)
            print(f"Error: {e}")
            return None

    def update_destination_data(self):
        # Ensure there is valid destination data before updating
        if not self.destination_data:
            print("No destination data to update.")
            return

        for city_name in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city_name['iataCode']
                }
            }
            try:
                # Make the PUT request to update the data
                response = requests.put(
                    url=f"{sheety_api_endpoint}/{city_name['id']}",
                    json=new_data,
                    headers=self.headers
                )

                # Check if the response is successful
                if response.status_code == 200:
                    print(f"Successfully updated data for {city_name['city']}.")
                else:
                    print(f"Failed to update data for {city_name['city']}. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                # Catch any errors with the PUT request
                print(f"Error while updating {city_name['city']}: {e}")

