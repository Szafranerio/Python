import requests


pixela_endpoint = 'https://pixe.la/v1/users'
USER = 'szafraneriooo'
TOKEN = 'vfbrgnthmyjntbrvetrbevs'


user_params = {
    'token': TOKEN,
    'username': USER,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}


#response = requests.post(url=pixela_endpoint, json=user_params)
#print("User creation response:", response.status_code, response.text)


graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graphs_params = {
    'id' : 'graph2',
    'name' : 'Pages of books',
    'unit' : 'pages',
    'type' : 'int',
    'color' : 'momiji' ,
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

graph_response = requests.post(url=graph_endpoint, json=graphs_params, headers = headers)
print(graph_response.text)

point_params = {
    'date' : '20240901',
    'quantity' : 2,
}
point_response = requests.post(url='https://pixe.la/v1/users/szafraneriooo/graphs/graph2)', json=point_params, headers=headers)
print(point_params)   