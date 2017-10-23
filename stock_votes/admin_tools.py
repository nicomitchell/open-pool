import sys
sys.path.append('C://Users/unorc/OneDrive/Documents/GitHub/VandyHacks/stock_votes/financial_data_tools')
from stock_classes import *
from create_transaction import create_transaction
import firebase_admin
from firebase_admin import db

# cred = credentials.Certificate('C://users/unorc/OneDrive/Documents/GitHub/open-pool-firebase-adminsdk-xc8y8-7b28bfb261.json')
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://open-pool.firebaseio.com'
# })
ref = db.reference('users')
