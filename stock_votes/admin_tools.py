import sys
sys.path.append('C://Users/unorc/OneDrive/Documents/GitHub/VandyHacks/stock_votes/financial_data_tools')
from stock_classes import *
import create_transaction
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# cred = credentials.Certificate('C://users/unorc/OneDrive/Documents/GitHub/open-pool-firebase-adminsdk-xc8y8-7b28bfb261.json')
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://open-pool.firebaseio.com'
# })
ref = db.reference('users')
#print(ref.get())

m = ref.child('robertmaxwilliams')
m.child('screen_name').set('Max Williams')

m = m.get()
max = user(m['userid'],m['email_address'],'59eb8d6eb390353c953a1565')
main_acc = user('Open-Pools','N/A','59eb79b5b390353c953a1555') #company account
print("Max balance: " + str(max.usd_balance) + "Co. balance: " + str(main_acc.usd_balance)) 
#create_transaction(max.bank_acc.url_base + "accounts/" + max.bank_acc.acc_id + "/transfers",'balance',main_acc.bank_acc.acc_id,10,"Test")
max.update()
main_acc.update()
print("New Max balance: " + str(max.usd_balance) + "New Co. balance: " + str(main_acc.usd_balance)) 