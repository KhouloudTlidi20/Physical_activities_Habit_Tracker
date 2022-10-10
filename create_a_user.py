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
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
