#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd 
import numpy as np
from weather import data
import datetime
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import requests
from dotenv import load_dotenv
import os

load_dotenv()


# In[16]:


OMW_ENDPOINT = os.getenv('OMW_ENDPOINT')
API_KEY = os.getenv('API_KEY')

weather_params = {
    'lat':  54.51,
    'lon': 18.53,
    'cnt': 8,
    'appid': API_KEY,
}
data = requests.get(OMW_ENDPOINT, params=weather_params)
data = data.json()
print(data)


# In[17]:


temp_max = [day['main']['temp_max'] for day in data['list']]
print(temp_max)


# In[18]:


date = data['list'][0]['dt']
dates = [day['dt'] for day in data['list']]
temp_max = [day['main']['temp_max'] for day in data['list']]
temp_max = [temp - 273.15 for temp in temp_max]
temp_min = [day['main']['temp_min'] for day in data['list']]
temp_min = [temp - 273.15 for temp in temp_min]
pressure = [day['main']['pressure'] for day in data['list']]
humidity = [day['main']['humidity'] for day in data['list']]
wind = [day['wind']['speed'] for day in data ['list']]


# In[19]:


def convert_utc_list(dates):
    return [datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H') for ts in dates]
converted_dates = convert_utc_list(dates)
for date in converted_dates:
    print(date)   
converted_dates = convert_utc_list(dates)
                 


# In[20]:


dict = {'Date': converted_dates, 'Temp_Max': temp_max, 'Temp_Min':temp_min, 'Humidity': humidity, 'Pressure': pressure, 'Wind_Speed': wind}
weather_forecast = pd.DataFrame(dict)
weather_forecast.set_index('Date', inplace=True)


# In[21]:


fig_temp = go.Figure()
fig_temp.add_trace(go.Scatter(x=weather_forecast.index, y=weather_forecast['Temp_Max'], mode='lines+markers', name='Max Temperature (°C)'))
fig_temp.update_traces(line_color='gold', fill='tozeroy')
fig_temp.update_layout(template='simple_white')
fig_temp.update_layout(width=1000, height=800)
fig_temp.write_image('temperature.png')
fig_temp.show()


# In[22]:


fig_hum = px.line(weather_forecast, x=weather_forecast.index, y='Humidity', template='simple_white')
fig_hum.update_yaxes(range=[0, weather_forecast['Humidity'].max()])
fig_hum.update_traces(line_color='yellowgreen', fill='tozeroy')
fig_hum.write_image('humidity.png')
fig_hum.show()


# In[26]:


fig_wind = px.line(weather_forecast, x=weather_forecast.index, y='Wind_Speed', template='simple_white')
fig_wind.update_traces(line_color='turquoise', fill='tozeroy')
fig_wind.write_image('windspeed.png')
fig_wind.show()


# In[ ]:




