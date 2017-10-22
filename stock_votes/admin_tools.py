import sys
sys.path.append('C://Users/unorc/OneDrive/Documents/GitHub/VandyHacks/stock_votes/financial_data_tools')
from stock_classes import *

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('C://users/unorc/OneDrive/Documents/GitHub/open-pool-firebase-adminsdk-xc8y8-7b28bfb261.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://open-pool.firebaseio.com'
})
ref = db.reference('users')
#print(ref.get())

m = ref.child('robertmaxwilliams')
m.child('screen_name').set('I love penis')

m = m.get()
print(m)
max = user(m['userid'],m['email_address'],'59eb8d6eb390353c953a1565')
#print(max.usd_balance)