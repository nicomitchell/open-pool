import json
import requests
from json_formatter import json_format

# api_key = 'a1e0eb837b518f02a40fb0319ba0c776'
# url = 'http://api.reimaginebanking.com/customers?key={}'.format(api_key)
# print(url)
# first_name = str(input("First: "))
# second_name = str(input("Last: "))
# street_number = str(input("Street Number: "))
# street_name = str(input("Street Name: "))
# city = str(input("City: "))
# state = str(input("State: "))
# zip_code = str(input("ZIP Code: "))

def make_customer(url,first_name,second_name,street_number,street_name,city,state,zip_code):
    new_customer = {
        "first_name": first_name,
        "last_name": second_name,
        "address": {
            "street_number": street_number,
            "street_name": street_name,
            "city": city,
            "state": state,
            "zip": zip_code
        }
    }
    response = requests.post(
        url,
        data = json.dumps(new_customer),
        headers = {'content-type' : 'application/json'}
        )
    return response.status_code

# response_status_code = make_customer(first_name,second_name,street_number,street_name,city,state,zip_code)
# if response_status_code == 201:
# 	print('Customer created')
# else:
#     print(response_status_code)

# r = requests.get(url)
# data = str(json.dumps(r.text))
# data = json_format(data)
# print(data)