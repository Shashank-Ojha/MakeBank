import requests
import json
#customer_url only has api key, no customer id

#create a new customer
customer_url="http://api.reimaginebanking.com/customers?key=3f5b7bf5eab502003796c17aa8e134e4"
new_customer= {
  "first_name": "teg",
  "last_name": "singh",
  "address": {
    "street_number": "309",
    "street_name": "Ashley Court",
    "city": "Oak Brook",
    "state": "IL",
    "money": "60523"
  }
}
#submit post request
# response = requests.post( 
#     customer_url, 
#     data=json.dumps(new_customer),
#     headers={'content-type':'application/json'},
#     )

customers=requests.get(customer_url)
customers_data=json.loads(customers.text)
print(customers_data)
for customer in customers_data:
    ID=customer["_id"]
    print(ID)
    delete_url="http://api.reimaginebanking.com/accounts/{}?key=3f5b7bf5eab502003796c17aa8e134e4".format(ID)
    r=requests.delete(
        delete_url,
        data=json.dumps(customer),
        headers={'content-type':'application/json'},
    )    
    print(r.status_code)
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