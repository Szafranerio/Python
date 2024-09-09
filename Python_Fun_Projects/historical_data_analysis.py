#!/usr/bin/env python
# coding: utf-8

# In[220]:


import pandas as pd 
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from historical_data_weather import data
import seaborn as sns
import numpy as np


# In[221]:


tempmax_data = data['days'][0]['tempmax']
print(tempmax_data)

tempmax_data_past_30 = [day['tempmax'] for day in data['days']]
tempmax_data_past_30 = pd.DataFrame({'TemperatureMax' : tempmax_data_past_30})
print(tempmax_data_past_30)

tempmin_data = data['days'][0]['tempmin']
print(tempmin_data)

tempmin_data_past_30 = [day['tempmin'] for day in data['days']]
tempmin_data_past_30 = pd.DataFrame({'TemperatureMin' : tempmin_data_past_30})
print(tempmin_data_past_30)

humidity_data = data['days'][0]['humidity']
print(humidity_data)

humidity_data_past_30 = [day['humidity'] for day in data['days']]
humidity_data_past_30 = pd.DataFrame({'Humidity': humidity_data_past_30})
print(humidity_data_past_30)

pressure_data = data['days'][0]['pressure']
print(pressure_data)

pressure_data_past_30 = [day['pressure'] for day in data['days']]
pressure_data_past_30 = pd.DataFrame({'Pressure': pressure_data_past_30})
print(pressure_data_past_30)

uv_index = data['days'][0]['uvindex']
print(uv_index)

uv_index_past_30 = [day['uvindex'] for day in data['days']]
uv_index_past_30 = pd.DataFrame({'UV_Index' : uv_index_past_30})
print(uv_index_past_30)

date = [day['datetime'] for day in data['days']]
date = pd.DataFrame({'Date': date})
print(date)


# In[222]:


historical_data = tempmax_data_past_30.join([tempmin_data_past_30, humidity_data_past_30, pressure_data_past_30, uv_index_past_30, date])
historical_data.set_index('Date')
historical_data.info()


# In[223]:


historical_data['Date'] = historical_data['Date'].astype({'Date': 'datetime64[ns]'})
historical_data.set_index('Date')


# In[224]:


sns.heatmap(historical_data.corr())


# In[225]:


#Lineplot tempmax and tempmin

fig_temp = go.Figure()

fig_temp.add_trace(go.Scatter(x=historical_data['Date'], y=historical_data['TemperatureMin'], name = 'Temp Min', mode='lines+markers', text=historical_data['TemperatureMin'], marker=dict(size=10)))
fig_temp.add_trace(go.Scatter(x=historical_data['Date'], y=historical_data['TemperatureMax'], name = 'Temp Max',mode='lines+markers', text=historical_data['TemperatureMax'],marker=dict(size=10)))

fig_temp.update_traces(textfont=dict(size=12))
fig_temp.update_traces(textposition = 'bottom center')
fig_temp.update_layout(template='simple_white')
fig_temp.update_layout(width=1300, height=800)
fig_temp.show()
fig_temp.write_image("/home/Szafranerio/temp_graph.png")


# In[226]:


fig_uv = px.line(historical_data, x='Date', y='UV_Index', template='simple_white')
fig_uv.update_yaxes(range=[0, historical_data['UV_Index'].max()])
fig_uv.update_traces(line_color='gold', fill='tozeroy')
fig_uv.show()
fig_uv.write_image("/home/Szafranerio/uv_graph.png")


# In[227]:


fig_hum = px.line(historical_data, x='Date', y='Humidity', template='simple_white')
fig_hum.update_yaxes(range=[0, historical_data['Humidity'].max()])
fig_hum.update_traces(line_color='yellowgreen', fill='tozeroy')
fig_hum.show()
fig_hum.write_image("/home/Szafranerio/hum_graph.png")

