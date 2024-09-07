import requests
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()

test = input('What did you do?: ')
AGE = int(input('What is your age?: '))
WEIGHT_KG = int(input('What is your weight?: '))
HEIGHT = float(input('What is your height?: '))


API_ID = os.getenv('API_ID')
API_KEY = os.getenv('API_KEY')

exercise_endpoint = os.getenv('exercise_endpoint')
sheety_endpoint = os.getenv('sheety_endpoint')

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
}

parameters = {
    'query': test,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT,
    'age': AGE
}


response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


# Auth
bearer_headers = {
    'Authorization': f"Bearer {'AalborgGdynia'}"
}
today_date = datetime.now().strftime('%d/%m/%y')
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_inputs = {
        'stat': {
            'date': today_date,
            'time': now_time,
            'exercise': exercise['name'],
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheet_response = requests.post(
        sheety_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
