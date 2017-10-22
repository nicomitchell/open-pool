import json
import requests

def create_transaction(url,medium,payee_id,amount,transaction_date,desc):
    payload = {
        "url" : url,
        "medium" : medium,
        "payee_id" : payee_id,
        "amount" : amount,
        "transaction_data" : transaction_date,
        "description" : desc
    }
    response = requests.post( 
		url, 
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
	)
    return response.status_code
