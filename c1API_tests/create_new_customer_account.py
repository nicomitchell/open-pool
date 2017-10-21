import json
import requests

customer_key = '59eb784cb390353c953a1554'
api_key = 'a1e0eb837b518f02a40fb0319ba0c776'
url = 'http://api.reimaginebanking.com/customers?key={}'.format(api_key)
print(url)
first_name = str(input("First: "))
second_name = str(input("Last: "))
street_number = str(input("Street Number: "))
street_name = str(input("Street Name: "))
city = str(input("City: "))
state = str(input("State: "))
zip_code = str(input("ZIP Code: "))

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
if response.status_code == 201:
	print('Customer created')
r = requests.get(url)
data = str(json.dumps(r.text))
data = data.replace(',',',\n')
print(data)