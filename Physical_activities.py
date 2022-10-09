import requests
from datetime import datetime
USERNAME = "khouloud"
TOKEN = "llkskoaoe7744dfbch"
pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

#Graph 1 for jogging (Km) & graph 2 for Burned calories

def jogging():
    GRAPH_ID = "graph1"
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

    today = datetime.now()
    today_pixel = today.strftime("%Y%m%d")

    pixel_data = {
        "date": today_pixel,
        "quantity": input("How much did I jog today?\n"),
    }

    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    print(response.text)

def burn_calories():
    GRAPH_ID = "graph2"
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

    today = datetime.now()
    today_pixel = today.strftime("%Y%m%d")

    pixel_data = {
        "date": today_pixel,
        "quantity": input("How much calories did I burn today?\n"),
    }

    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    print(response.text)

def update_values():
    GRAPH_ID = "graph1"
    today = datetime.now()
    today_pixel = today.strftime("%Y%m%d")
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_pixel}"
    now_pixel_data = {
        "quantity": input("How much did I jog today?\n"),
    }
    response = requests.put(url=update_endpoint, json=now_pixel_data, headers=headers)
    print(response.text)
    GRAPH_ID = "graph2"
    today = datetime.now()
    today_pixel = today.strftime("%Y%m%d")
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_pixel}"
    now_pixel_data = {
        "quantity": input("How much calories did I burn today?\n"),
    }
    response = requests.put(url=update_endpoint, json=now_pixel_data, headers=headers)
    print(response.text)
jogging()
burn_calories()
update = input("Do you want to update something? y or n. \n").lower()
if update == "y":
    update_values()
