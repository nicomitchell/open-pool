import json
import urllib.request

# cust_IDs = ['59eae941a73e4942cdafe3ba', '59eae940a73e4942cdafe3b8','59eae941a73e4942cdafe3b9','59eb784cb390353c953a1554','59eb7ee4b390353c953a1559','59eb7f64b390353c953a155b','59eb8bffb390353c953a1561']
# apiKey = 'a1e0eb837b518f02a40fb0319ba0c776'
# f = open('customers.json','w')

def json_format(str):
    return str.replace('},{','\n\t},\n\t{\n\t\t').replace(',',',\n\t\t').replace('}]','\n\t}\n]').replace('[{','[\n\t{\n\t\t')

# for cust in cust_IDs:
#     url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(cust,apiKey)
#     r = urllib.request.urlopen(url)
#     txt = r.read().decode('utf-8')
#     txt  = json_format(txt)
#     print(txt)
#     f.write(txt + '\n\n')

# f.close()