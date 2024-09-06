import requests
import smtplib
import os

# PLACE API PARAMETERS


# Location is set up to fit Gdynia region in Poland, change lat and lon.
weather_params = {
    'lat':  54.51,
    'lon': 18.53,
    'cnt': 4,
}

data = requests.get(OMW_Endpoint, params=weather_params)
data = data.json()
temp_data = data['list'][0]['main']['temp']
cel_temp = temp_data - 273.15
cel_temp = round(cel_temp)

will_rain = False

# Specific raining infomatons:
for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if 200 < int(condition_code) <= 700:
        will_rain = True
        break

if will_rain:
    print('Bring umbrela')
else:
    print(f'Nice weather, temperature will be around {cel_temp}')

# Mailing
mail = 'enter_your_mail'
password = 'enter_your_password'

subject = 'Subject:Weather Forecast for today\n\n'
if will_rain:
    body = f'It is going to rain today, temperature will be around {cel_temp}'
else:
    body = f'It will be sunny today, temperature will be around {cel_temp}'

# Remeber to change the security options!!!
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=mail, password=password)
    connection.sendmail(
        from_addr=mail, to_addrs='enter_the_mail_here', msg=subject + body)
print('Email was sent')
