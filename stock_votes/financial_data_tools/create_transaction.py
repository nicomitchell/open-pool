import json
import requests

def create_transaction(url,payee_id,amount,transaction_date,desc):
    payload = {
        "medium" : "balance",
        "payee_id" : payee_id, 
        "amount" : amount,
        "transaction_date" : transaction_date,
        "description" : desc
    }
    response = requests.post( 
		url, 
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
	)
    return response.content