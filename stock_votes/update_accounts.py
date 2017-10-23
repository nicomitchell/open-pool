import json
from financial_data_tools.stock_classes import *
from financial_data_tools.create_transaction import create_transaction
from firebase_admin import db
users = db.reference('users')
u_list = list()
for u in users.get():
    if users.get()[u]['acc_id'] != None:
         u_list.append(user(users.get()[u]['userid'],users.get()[u]['email_address'],users.get()[u]['acc_id']))
    else:
         u_list.append(user(users.get()[u]['userid'],users.get()[u]['email_address']))

for i in u_list:
    print(i.user_id)
