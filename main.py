import os
import requests
import datetime as dt

today = dt.datetime.now()
NOW = today.strftime("%m/%d/%Y")
TIME = today.strftime("%r")


APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

EXERSICE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETS_URL = os.environ["SHEETS_URL"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
# input("What workout did you do today? ")
params = {
    "query": input("What was your workout today? "),
    "gender": "male",
    "weight_kg": 72.57,
    "height_cm": 182.88,
    "age": 24
}

response = requests.post(url=EXERSICE_URL, headers=headers, json=params)
response.raise_for_status()
data = response.json()

exercise = (data["exercises"][0]['name'].title())
duration = (data["exercises"][0]['duration_min'])
calories = (data["exercises"][0]['nf_calories'])

if exercise == "Weight Lifting" or exercise == "Squats":
    weight = input("How many pounds? ")
    sets = input("How many sets? ")
    reps = input("How many reps per set? ")

    inputs = {
        "workout": {
            "time": TIME,
            "date": NOW,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
            "weight": weight,
            "sets": sets,
            "reps": reps,
        }
    }
else:
    inputs = {
        "workout": {
            "time": TIME,
            "date": NOW,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

sheet_headers = {
    "Authorization": "os.environ['sheet_code']"
}


res = requests.post(url=SHEETS_URL, json=inputs, headers=sheet_headers)

