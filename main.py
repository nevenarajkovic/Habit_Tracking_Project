import requests
from datetime import datetime

from requests import delete

USERNAME = "nevena"
TOKEN = "hejhejaoaksnlnda"

GRAPH_ID = "graph1"

# Base Pixela API endpoint
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment this block ONLY if the user does not exist yet
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# Endpoint for creating graphs for the  user
qraph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


# Configuration of the graph
# This graph tracks cycling distance in kilometers
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"

}


# Authentication header required by Pixela
headers = {
    "X-USER-TOKEN": TOKEN
}
# Uncomment this block ONLY ONCE to create the graph
# response = requests.post(url=qraph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Endpoint for adding a pixel to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Get today's date
today = datetime.now()
# print(today.strftime("%Y-%m-%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),  # characters of the year, month and day
    "quantity": input("How many kilometers did you cycle today? "),  #this is the number of kilometers cycled
}

# Create a new pixel for today
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Endpoint for updating today's pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# New value for the pixel
new_pixel_data = {
    "quantity": "4.5"
}

# Update the existing pixel
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)


# Endpoint for deleting today's pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


# Uncomment this block if you want to delete the pixel
#response = requests.delete(url=delete_endpoint, headers=headers)
#print(response.text)





