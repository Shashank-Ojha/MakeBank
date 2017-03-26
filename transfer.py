import requests
import json
from is_borrower import *
from is_lender import *

def get_account_balance(customer):
    account_url="http://api.reimaginebanking.com/customers/{}/accounts?key=dcd6272d8dab8b826b5c1376ac90af1b".format(customer["_id"])
    response=requests.get(account_url)
    response=json.loads(response.text)
    response=response[0]
    return response["balance"]

class Lender(object):
    def __init__(self, name, lend_amount, lend_interest_rate, customer_id):
        self.name=name
        self.lend_amount=lend_amount
        self.lend_interest_rate=lend_interest_rate
        customer_url="http://api.reimaginebanking.com/customers/{}?key=dcd6272d8dab8b826b5c1376ac90af1b".format(customer_id)
        customer=requests.get(customer_url)
        customer=json.loads(customer.text)
        self.customer=customer  #capital one dictionary for get customers
        self.account_balance=get_account_balance(customer)


#hardcoded for now to make a borrower named lender, who is already stored in captial 1 database
def make_lender(lend_amount, lend_interest_rate, name):
    customers_url="http://api.reimaginebanking.com/customers?key=dcd6272d8dab8b826b5c1376ac90af1b"
    customers=requests.get(customers_url)
    customers=json.loads(customers.text)
    customer_id=None
    for customer in customers:
        if customer["first_name"]==name:
            customer_id=customer["_id"]
    # if customer_id==None:
        #do something
    Lender=Lender(name, lend_amount, lend_interest_rate, customer_id)
    return Lender


#payer is the lender, aka lender lenny
customer_url="http://api.reimaginebanking.com/customers?key=dcd6272d8dab8b826b5c1376ac90af1b"
customers=requests.get(customer_url)
customers=json.loads(customers.text)
for customer in customers:
    if customer["first_name"]=="Lender":
        payer_id=customer["_id"]

account_url="http://api.reimaginebanking.com/customers/{}/accounts?key=dcd6272d8dab8b826b5c1376ac90af1b".format(payer_id)
payer_account=requests.get(account_url)
payer_account=json.loads(payer_account.text)[0]
payer_account_id=payer_account["_id"]

def transferMoney(borrower, lender_lend_amount, lender_lend_interest_rate): #get borrower as an object of is_borrower
    # payee_customer_id=borrower.customer["_id"]
    # account_url="http://api.reimaginebanking.com/customers/{}/accounts?key=dcd6272d8dab8b826b5c1376ac90af1b".format(payee_customer_id)
    # payee_account=requests.get(account_url)
    # payee_account=json.loads(payee_account.text)
    # payee_account=borrower.account_id
    # transfer_url="http://api.reimaginebanking.com/accounts/{}/transfers?key=dcd6272d8dab8b826b5c1376ac90af1b".format(payer_account_id)
    # transfer_body={
    #   "medium": "balance",
    #   "payee_id": payee_account,
    #   "amount": borrower.borrow_amount+0.00,
    #   "transaction_date": "2017-03-26",
    # }
    # response = requests.post(
    #     transfer_url,
    #     data=json.dumps(transfer_body),
    #     headers={'content-type':'application/json'},
    #     )
    lender=make_lender(lender_lend_amount, lender_lend_interest_rate,"Lender")
    lender.account_balance=lender.account_balance-borrower.borrow_amount+0.00
    return lender.account_balance
