import requests
import datetime as dt

nutrionix_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrionix_api_id = "828d8f59"
nutrionix_api_key = "5bbf960341f796b225325188794fb43a"

sheety_api_endpoint = "https://api.sheety.co/1be0483e92ce611e6b5943d8a8f58ca7/myWorkouts/workouts"

headers = {
    "x-app-id": nutrionix_api_id,
    "x-app-key": nutrionix_api_key,
    "Content-Type": "application/json"
}

data = {
    "query": input("Tell me which exercises you did: ")
}

response = requests.post(url=nutrionix_api_endpoint, json=data, headers=headers)
result = response.json()['exercises']

exercise = response.json()['exercises'][0]['name'].title()
duration = response.json()['exercises'][0]['duration_min']
calories = response.json()['exercises'][0]['nf_calories']

today = dt.datetime.now()

for exercise in result:
    sheet_data = {
        "workout" : {
            "date" : today.strftime("%d%m%Y"),
            "time" : today.strftime("%X"),
            "exercise" : exercise['name'].title(),
            "duration" : exercise['duration_min'],
            "calories" : exercise['nf_calories']
            }
        }

    sheet_response = requests.post(url=sheety_api_endpoint,json=sheet_data)

    print(sheet_response.text)



