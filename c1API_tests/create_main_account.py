import json
import requests

customer_key = '59eb784cb390353c953a1554'
api_key = 'a1e0eb837b518f02a40fb0319ba0c776'
url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customer_key,api_key)

account = {
  "type": "Checking",
  "nickname": "Company account",
  "rewards": 0,
  "balance": 200000,	
}

response = requests.post( 
	url, 
	data=json.dumps(account),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('account created')
r = requests.get(url)
data = str(json.dumps(r.text))
print(data)