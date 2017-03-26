import requests
import json
from is_borrower import *


#payer is the lender, aka lender lenny
customer_url="http://api.reimaginebanking.com/customers?key=dcd6272d8dab8b826b5c1376ac90af1b"
customers=requests.get(customer_url)
customers=json.loads(customers.text)
for customer in customers:
    if customer["first_name"]=="Lender":
        payer_id=customer["_id"]

account_url="http://api.reimaginebanking.com/customers/{}/accounts?key=dcd6272d8dab8b826b5c1376ac90af1b".format(payer_id)
payer_account=requests.get(account_url)
payer_account=json.loads(payer_account.text)
payer_account=payer_accound["_id"]

def transfer(borrower): #get borrower as an object of is_borrower
    