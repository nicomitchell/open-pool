import json
import requests
from json_format_customers import json_format
# customer_key = '59eba6e7b390353c953a1588'
# api_key = 'a1e0eb837b518f02a40fb0319ba0c776'
# url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customer_key,api_key)


# a_type = str(input("Account type: "))
# a_name = str(input("Account name: "))
# a_rewards = float(input("Rewards: "))
# a_balance = float(input("Balance: "))

def make_new_account(url,a_type,a_name,a_rewards,a_balance):
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
	return response.status_code

# response_status_code = make_new_account(a_type,a_name,a_rewards,a_balance)

# if response_status_code == 201:
# 	print('account created')
# else:
# 	print("Response Code: " + response_status_code)
# r = requests.get(url)
# data = str(json.dumps(r.text))
# print(json_format(data))