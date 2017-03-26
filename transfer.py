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
<<<<<<< HEAD
payer_account=json.loads(payer_account.text)
=======
payer_account=json.loads(payer_account.text)[0]
>>>>>>> origin/master
payer_account_id=payer_account["_id"]

def transferMoney(borrower): #get borrower as an object of is_borrower
    # payee_customer_id=borrower.customer["_id"]
    # account_url="http://api.reimaginebanking.com/customers/{}/accounts?key=dcd6272d8dab8b826b5c1376ac90af1b".format(payee_customer_id)
    # payee_account=requests.get(account_url)
    # payee_account=json.loads(payee_account.text)
    payee_account=borrower.account_id
    transfer_url="http://api.reimaginebanking.com/accounts/{}/transfers?key=dcd6272d8dab8b826b5c1376ac90af1b".format(payer_account_id)
    transfer_body={
      "medium": "balance",
      "payee_id": payee_account,
      "amount": borrower.borrow_amount+0.00,
      "transaction_date": "2017-03-26",
    }
    response = requests.post(
        transfer_url,
        data=json.dumps(transfer_body),
        headers={'content-type':'application/json'},
        )

    return payer_account["balance"]
