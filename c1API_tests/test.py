
#import requests
import json
import urllib.request

cust_IDs = ['59eae941a73e4942cdafe3ba', '59eae940a73e4942cdafe3b8','59eae941a73e4942cdafe3b9']
apiKey = 'a1e0eb837b518f02a40fb0319ba0c776'
f = open('customers.json','w')

for cust in cust_IDs:
    url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(cust,apiKey)
    r = urllib.request.urlopen(url)
    txt = r.read().decode('utf-8')
    txt = txt.replace(',',',\n')
    print(txt)
    f.write(txt + '\n\n')

f.close()