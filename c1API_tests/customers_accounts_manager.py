import json
import requests
from create_account import make_new_account
from create_new_customer import make_customer
from json_format_customers import json_format

api_key = "a1e0eb837b518f02a40fb0319ba0c776"
url_base = "http://api.reimaginebanking.com/"
while(True):
    print("1) View Customers\n" +
        "2) View Accounts\n" +
        "3) Add Customer\n" +
        "4) Add Account\n" +
        "5) Exit\n")

    choice = int(input("What would you like to do?\t"))

    if choice == 1:
        url = '%scustomers?key=%s' % (url_base,api_key)
        response = requests.get(url)
        print("Customers: \n" + json_format(str(json.dumps(response.text))))
        print("Process complete.")
    elif choice == 2:
        url = '%saccounts?key=%s' %(url_base,api_key)
        response = requests.get(url)
        print("Accounts: \n" + json_format(str(json.dumps(response.text))))
        print("Process complete.")
    elif choice == 3:
        first_name = str(input("First: "))
        second_name = str(input("Last: "))
        street_number = str(input("Street Number: "))
        street_name = str(input("Street Name: "))
        city = str(input("City: "))
        state = str(input("State: "))
        zip_code = str(input("ZIP Code: "))
        url = '%scustomers?key=%s' % (url_base,api_key)
        response_code = make_customer(url,first_name,second_name,street_number,street_name,city,state,zip_code)
        if response_code != 201:
            print("Customer could not be created. Response code: " + str(response_code))
        else:
            print("Customer created successfully!")
    elif choice == 4:
        customer_key = str(input("Unique Customer PIN: "))
        url = '%scustomers/%s/accounts?key=%s' % (url_base,customer_key,api_key)
        if requests.get(url).status_code == 200:
            a_type = str(input("Account type: "))
            a_name = str(input("Account name: "))
            a_rewards = float(input("Rewards: "))
            a_balance = float(input("Balance: "))
            response_code = make_new_account(url,a_type,a_name,a_rewards,a_balance)
            if response_code != 201:
                print("Account could not be created. Response code: " + str(response_code))
            else:
                print("Account created successfully!")
        else:
            print("ID could not be found.")
    else:
        break
