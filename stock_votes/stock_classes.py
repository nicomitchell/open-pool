import json
import requests

class bank_account(object):
    url_base = 'http://api.reimaginebanking.com/'
    api_key = 'a1e0eb837b518f02a40fb0319ba0c776'
 
    def __init__(self,acc_id):
        if acc_id == 0:
            self.response = {'balance' : 0,'type' : 0, 'rewards' : 0, 'customer_id' : 0,'_id' : 0,'nickname' : 0}
        self.url = '%saccounts/%s?key=%s' % (self.url_base,acc_id,self.api_key)
        self.response = json.loads(requests.get(self.url).text)
    #Returns .json dictionary
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



class user(object):
    def __init__(self,screen_name,email_address,acc_id = '0'):
        self.screen_name = screen_name
        self.email_address = email_address
        self.bank_acc = None
        self.usd_balance = 0
        if acc_id != '0':
            self.link_bank_account(acc_id)
    def link_bank_account(self,acc_id):
        self.bank_acc = bank_account(acc_id)
        self.usd_balance = self.bank_acc.get_balance()


class pool(object):
    def __init__(self,creator,total_value,begin_conditions = list(),
                end_conditions  = list(),stock_options = list()):
        self.creator = creator
        self.investments = [investment(creator,total_value,self)]
        self.total_value = total_value
        self.begin_conditions = begin_conditions
        self.end_conditions = end_conditions
        self.stock_options = stock_options
    def add_investment(self,investment):
        self.investments.append(investment)
        self.total_value += investment.value

class investment(object):
    def __init__(self,user,value,pool):
        self.investor = user
        self.value = value
        self.pool = pool


# item = bank_account('59eb79b5b390353c953a1555')
# print(item.get_acc_id())
# print(item.get_acc_nickname())
# print(item.get_account_type())
# print(item.get_balance())
# print(item.get_customer_id())
# print(item.get_rewards())

# nico = user('Nico','namitc02@louisville.edu','59eb8d1ab390353c953a1563')
# print(nico.screen_name + " " + nico.email_address + " " + str(nico.usd_balance))

# p = pool(nico,20.00)

# max_ = user('Max','fakeemail','59eb8d6eb390353c953a1565')

# i = investment(max_,22.00,p)
# p.add_investment(i)

# for i in p.investments:
#     print (i.investor.screen_name + " " + str(i.value))
# print(p.total_value)