import requests
import json
#ONLY LOAD THIS PAGE ONCE
#ASK TEG AND RIYA IF U NEED TO CHANGE SOMETHING HERE


teg_api="dcd6272d8dab8b826b5c1376ac90af1b"
customer_url="http://api.reimaginebanking.com/customers?key=dcd6272d8dab8b826b5c1376ac90af1b"
new_customer= {
  "first_name": "Adam",
  "last_name": "Appleseed",
  "address": {
    "street_number": "111",
    "street_name": "Avalanche Road",
    "city": "Austin",
    "state": "AK",
    "money": "11111"
  }
}

#submit post request
response = requests.post( 
    customer_url, 
    data=json.dumps(new_customer),
    headers={'content-type':'application/json'},
    )
print(response.status_code)

