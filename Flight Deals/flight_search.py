import requests

amadeus_api_endpoint = "https://test.api.amadeus.com/v1/shopping/flight-dates"
amadeus_api_key = "xrXnq0kIjDgMWGQ0tnVtkO7fDIZJVHZA"
amadeus_api_secret = "bR9966ToSD9s35Ts"

access_token_server = "https://test.api.amadeus.com/v1/security/oauth2/token"

access_token = 'o6WoAbSfC7kCAGYKhOxxU1jFl29u'

# Define the headers
amadeus_headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}


# Define the data (form parameters)
# data = {
#     'grant_type': 'client_credentials',
#     'client_id': amadeus_api_key,
#     'client_secret': amadeus_api_secret
# }
#
# response = requests.post(url=access_token_server,headers=headers,data=data)
#
# if response.status_code == 200:
#     token = response.json()
#     print(token)
# else:
#     print(f"Error:{response.status_code}")
#     print(response.text)

flight_api_endpoint = "https://test.api.amadeus.com/v1/shopping/flight-destinations"

headers = {
    'Authorization': f'Bearer {access_token}'
}
params = {
    'origin': 'PAR',  # Origin airport code (paris)
    'maxPrice': 200   # Maximum price
}

response = requests.get(url=flight_api_endpoint,headers=headers,params=params)

if response.status_code == 200:
    # Parse and print the response JSON
    data = response.json()
    print("Response Data:", data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)


# class FlightSearch:
#     #This class is responsible for talking to the Flight Search API.
#     pass