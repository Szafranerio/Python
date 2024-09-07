import requests
import smtplib
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
from datetime import datetime, timedelta


# Calculate today's date
today = datetime.now()

# Calculate the date 30 days ago
start_date = today - timedelta(days=30)

# Format the dates in the required format (YYYY-MM-DD)
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = today.strftime('%Y-%m-%d')

# Construct the API URL
api_key = '7WZ9R4RHHX4HFNNT87ZMCW5T8'

url = (f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/54.51%2C%2018.53/{start_date_str}/{end_date_str}'
       f'?unitGroup=metric&include=days&key={api_key}&contentType=json')

# Make the request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}, {response.text}')


temp_data = data['days'][0]['temp']
print(temp_data)

temp_data_past_30 = [day['temp'] for day in data['days']]
print(temp_data_past_30)

humidity_data = data['days'][0]['humidity']
print(humidity_data)

humidity_data_past_30 = [day['humidity'] for day in data['days']]
print(humidity_data_past_30)

pressure_data = data['days'][0]['pressure']
print(pressure_data)

pressure_data_past_30 = [day['pressure'] for day in data['days']]
print(pressure_data_past_30)

windspeed_data = data['data'][0]['windspeed']
print(windspeed_data)

windspeed_data_past_30 = [day['windspeed'] for day in data['days']]
print(windspeed_data_past_30)
