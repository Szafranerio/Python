import requests


pixela_endpoint = 'https://pixe.la/v1/users'
USER = 'szafranerio9'
TOKEN = 'dasgfwagresvscsv'


user_params = {
    'token': TOKEN,
    'username': USER,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}


response = requests.post(url=pixela_endpoint, json=user_params)
print("User creation response:", response.status_code, response.text)
