import requests

# Get a fresh token
url = "https://test.api.amadeus.com/v1/security/oauth2/token"
payload = {
    "grant_type": "client_credentials",
    "client_id": "xrXnq0kIjDgMWGQ0tnVtkO7fDIZJVHZA",  # Replace with your actual Client ID
    "client_secret": "bR9966ToSD9s35Ts"  # Replace with your actual Client Secret
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    access_token = response.json()["access_token"]
    print("New Access Token:", access_token)

    # Use the new token in your next request for the test environment
    city_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"  # Use test endpoint here
    params = {
        "keyword": "Paris",
        "include": "AIRPORTS"
    }
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    city_response = requests.get(city_url, headers=headers, params=params)

    if city_response.status_code == 200:
        print(city_response.json())
    else:
        print(f"City Request Error: {city_response.status_code} - {city_response.text}")
else:
    print(f"Error: {response.status_code} - {response.text}")
