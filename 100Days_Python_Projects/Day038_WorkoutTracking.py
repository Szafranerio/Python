import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Fetch environment variables
API_ID = os.getenv('API_ID')
API_KEY = os.getenv('API_KEY')
exercise_endpoint = os.getenv('exercise_endpoint')
sheety_endpoint = os.getenv('sheety_endpoint')


# Collect input from user
test = input('What did you do?: ')
AGE = int(input('What is your age?: '))
WEIGHT_KG = int(input('What is your weight?: '))
HEIGHT = float(input('What is your height?: '))

# Set headers and parameters for exercise API
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

# Make request to exercise API
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
if response.status_code != 200:
    print(f"Error with exercise API request: {response.text}")
    exit()

result = response.json()

# Auth header 
bearer_headers = {
    'Authorization': f"Bearer {'AalborgGdynia'}"  
}

# Collect current date and time
today_date = datetime.now().strftime('%d/%m/%y')
now_time = datetime.now().strftime("%X")

# Send data to Sheety API
for exercise in result.get('exercises', []):
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

    if sheet_response.status_code != 200:
        print(f"Error with Sheety API request: {sheet_response.text}")
    else:
        print(sheet_response.text)
