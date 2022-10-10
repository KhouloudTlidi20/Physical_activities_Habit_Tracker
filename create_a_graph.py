import requests
USERNAME = "khouloud"
TOKEN = "your_token"
GRAPH_ID = "graph10"
pixela_endpoint = "https://pixe.la/v1/users"

#Create a user
user_params = {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes",
}

#Create a graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Burn calories Graph",
    "unit": "Kcal",
    "type": "float",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
