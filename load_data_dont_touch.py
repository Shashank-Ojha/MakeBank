import requests
import json
import random
#ONLY LOAD THIS PAGE ONCE
#ASK TEG AND RIYA IF U NEED TO CHANGE SOMETHING HERE


# teg_api="dcd6272d8dab8b826b5c1376ac90af1b"
customer_url="http://api.reimaginebanking.com/customers?key=dcd6272d8dab8b826b5c1376ac90af1b"
new_customer= {
  "first_name": "Teg",
  "last_name": "El",
  "address": {
    "street_number": "666",
    "street_name": "Rocky Road",
    "city": "San Antonio",
    "state": "TX",
    "zip": "666666"
  }
}

response=requests.post(
  customer_url,
  data=json.dumps(new_customer),
  headers={'content-type':'application/json'}
  )
print(response.status_code)
# #new merchant
# url="http://api.reimaginebanking.com/merchants?key=3f5b7bf5eab502003796c17aa8e134e4"
# store={
#   "name": "Gap",
#   "category": [
#   "Clothing"
#   ],
#   "address": {
#     "street_number": "444",
#     "street_name": "Dee Road",
#     "city": "Pittsburgh",
#     "state": "PA",
#     "zip": "44444"
#   },
#   "geocode": {
#     "lat": 4,
#     "lng": 4
#   }
# }
# response = requests.post( 
#     url, 
#     data=json.dumps(store),
#     headers={'content-type':'application/json'},
#     )
# print(response.status_code)

# customer_id="58d6b0fa1756fc834d90658e"
# url="http://api.reimaginebanking.com/customers/{}/accounts?key=dcd6272d8dab8b826b5c1376ac90af1b".format(customer_id)

# account={
#   "type": "Credit Card",
#   "nickname": "Carlisle",
#   "rewards": 0,
#   "balance": 10000,
#   "account_number": "3333333333333333"
# }

# response = requests.post( 
#     url, 
#     data=json.dumps(account),
#     headers={'content-type':'application/json'},
#     )
# print(response.status_code)


#adam
# customer_id="58d6bffc1756fc834d9066a8"
# url="http://api.reimaginebanking.com/accounts/{}/purchases?key=dcd6272d8dab8b826b5c1376ac90af1b".format(customer_id)

# r=requests.get(url)
# re=json.loads(r.text)
# print(re)
# # for entry in re:
# #   ID=entry["_id"]
# #   purchase_url="http://api.reimaginebanking.com/purchases/{}?key=dcd6272d8dab8b826b5c1376ac90af1b".format(ID)
# #   for i in range(1,52,10):
# #     purchase={
# #       "description": "personal"
# #     }
# #     response = requests.put( 
# #       purchase_url, 
# #       data=json.dumps(purchase),
# #       headers={'content-type':'application/json'},
# #       )
# #     print(response.status_code)


# customer_id="58d6bffc1756fc834d9066a8"
# purchase_url="http://api.reimaginebanking.com/accounts/{}/purchases?key=dcd6272d8dab8b826b5c1376ac90af1b".format(customer_id)

# for i in range(1,52,10):
#   purchase={
#     "description": "personal"
#   }
#   response = requests.put( 
#     purchase_url, 
#     data=json.dumps(purchase),
#     headers={'content-type':'application/json'},
#     )
#   print(response.status_code)





