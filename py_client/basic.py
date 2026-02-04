import requests
import json

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/"
endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, json={"query": "Hello World"}) # HTTP request
print(get_response.text) # print raw text response
print(get_response.status_code)

# HTTP request --> HTML
# REST API request --> JSON

print(get_response.json())
