import requests
import json


#create a new customer
url="http://api.reimaginebanking.com/customers?key=3f5b7bf5eab502003796c17aa8e134e4"
new_customer= {
  "first_name": "teg",
  "last_name": "singh",
  "address": {
    "street_number": "309",
    "street_name": "Ashley Court",
    "city": "Oak Brook",
    "state": "IL",
    "zip": "60523"
  }
}
#submit post request
response = requests.post( 
    url, 
    data=json.dumps(new_customer),
    headers={'content-type':'application/json'},
    )

customers=requests.get(url)
customers_data=json.loads(customers.text)
for customer in customers_data:
    print(customer)
    break

# if response.status_code == 201:
#     print('new customer created')
# print (response)


# apiKey = '3f5b7bf5eab502003796c17aa8e134e4'

# url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
# payload = {
#   "type": "Savings",
#   "nickname": "test",
#   "rewards": 10000,
#   "balance": 10000, 
# }
# # Create a Savings Account
# response = requests.post( 
#     url, 
#     data=json.dumps(payload),
#     headers={'content-type':'application/json'},
#     )

# if response.status_code == 201:
#     print('account created')

# print (response.status_code)