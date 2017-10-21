import json
import requests

customer_key = '59eb8bffb390353c953a1561'
api_key = 'a1e0eb837b518f02a40fb0319ba0c776'
url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customer_key,api_key)


a_type = str(input("Account type: "))
a_name = str(input("Account name: "))
a_rewards = int(input("Rewards: "))
a_balance = int(input("Balance: "))
account = {
  "type": a_type,
  "nickname": a_name,
  "rewards": a_rewards,
  "balance": a_balance
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