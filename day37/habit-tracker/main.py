import os
import requests
import datetime


PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
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

header_config = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "page",
    "type": "int",
    "color": "kuro"
}

# res_graph = requests.post(url=graph_endpoint,json=graph_config,headers=header_config)
# print(res_graph.text)

today = datetime.datetime.now()
kusa_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "100"
}

kusa_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# res_kusa = requests.post(url=kusa_endpoint,json=kusa_config,headers=header_config)
# print(res_kusa.text)

delete_date="20220117"
delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date}"
#
# res_delete = requests.delete(url=delete_endpoint, headers=header_config)
# print(res_delete.text)

put_date = today.strftime("%Y%m%d")
today = datetime.datetime.now()
put_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{put_date}"
put_config = {
    "quantity": input("How many pages did you read today??")
}

res_put = requests.put(url=put_endpoint,json=put_config, headers=header_config)
print(res_put.text)

