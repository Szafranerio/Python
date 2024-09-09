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