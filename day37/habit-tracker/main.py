import os
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.getenv("PIXELA_USER")
TOKEN = os.getenv("PIXELA_TOKEN")
param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# res = requests.post(url=PIXELA_ENDPOINT, json=param)
# print(res.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_header_config = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "page",
    "type": "int",
    "color": "kuro"
}

# res_graph = requests.post(url=graph_endpoint,json=graph_config,headers=graph_header_config)
# print(res_graph.text)