import json
import requests
import sys
sys.path.append('C://users/unorc/OneDrive/Documents/GitHub/VandyHacks/stock_votes/financial_data_tools')
from create_transaction import create_transaction
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('C://users/unorc/OneDrive/Documents/GitHub/open-pool-firebase-adminsdk-xc8y8-7b28bfb261.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://open-pool.firebaseio.com'
})
ref = db.reference('users')
#links to Capital One Nessie api
class bank_account(object):
    url_base = 'http://api.reimaginebanking.com/'
    api_key = 'a1e0eb837b518f02a40fb0319ba0c776'
 
    def __init__(self,acc_id):
        if acc_id == 0:
            self.response = {'balance' : 0,'type' : 0, 'rewards' : 0, 'customer_id' : 0,'_id' : 0,'nickname' : 0}
        self.url_acc = '%saccounts/%s?key=%s' % (self.url_base,acc_id,self.api_key)
        self.response = json.loads(requests.get(self.url_acc).text)
        self.acc_id = acc_id
    def get_response(self):
        return self.response
    def get_balance(self):
        return self.response['balance']
    def get_account_type(self):
        return self.response['type']
    def get_rewards(self):
        return self.response['rewards']
    def get_customer_id(self):
        return self.response['customer_id']
    def get_acc_id(self):
        return self.response['_id']
    def get_acc_nickname(self):
        return self.response['nickname']
    def update(self):
        self.response = json.loads(requests.get(self.url_acc).text)
    def perform_transaction(self,value,target,desc):
        url = '%stransfers?key=%s' % (url_base,api_key)
        medium = 'balance'
        payee_id = target.get_acc_id()
        return create_transaction(url,medium,payee_id,value,desc)


class user(object):
    def __init__(self,user_id,email_address,acc_id = '0'):
        self.user_id = user_id
        self.email_address = email_address
        self.bank_acc = None
        self.usd_balance = 0
        self.btc_balance = 0
        self.ether_balance = 0
        self.active_investments = list()
        self.acc_id = '0'
        if acc_id != '0':
            self.link_bank_account(acc_id)
    def link_bank_account(self,acc_id):
        self.acc_id = acc_id
        self.bank_acc = bank_account(acc_id)
        self.usd_balance = self.bank_acc.get_balance()
    def invest(self,pool,value):
        i = investment(self,value,pool)
    def update(self):
        self.link_bank_account(self.acc_id)
        return self.usd_balance
    def updateDB(self):
        firebase_reference = db.reference('users')
        firebase_reference.child(self.user_id).set({
            'email_address' : self.email_address,
            'picture' : firebase_reference.child('picture').get(),
            'screen_name' : firebase_reference.child('screen_name').get(),
            'token' : firebase_reference.child('token').get(),
            'usd_balance' : self.usd_balance,
            'btc_balance' : self.btc_balance,
            'ether_balance' : self.ether_balance,
            'userid' : self.user_id
            }
        )


class pool(object):
    def __init__(self,name,creator,total_value,begin_conditions = list(),
                end_conditions  = list(),stock_options = list()):
        self.name = name
        self.creator = creator
        self.investments = [investment(creator,total_value,self)]
        self.total_value = total_value
        self.begin_conditions = begin_conditions
        self.end_conditions = end_conditions
        self.stock_options = stock_options
    def updateDB(self):
        firebase_reference = db.reference('pools')
        firebase_reference.child(self.name).set( {
            'assets_suggestions' : self.stock_options,
            'creator' : self.creator.user_id,
            'max' : firebase_reference.child('max').get(),
            'name' : self.name,
            'number_investors' : len(self.investments)
            }
        )


class investment(object):
    def __init__(self,user,value,pool):
        self.investor = user
        self.value = value
        self.pool = pool
        pool.investments.append(self)
        pool.total_value += value
        user.active_investments.append(pool)
        desc = "Investment:\n" + user.screen_name + " : $" + value + " to " + pool.name
        user.bank_acc.perform_transaction(value,"""MAINACC""",desc) 

