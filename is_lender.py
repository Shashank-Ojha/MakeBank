import requests
import json

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


#hardcoded for now to make a borrower named adam, who is already stored in captial 1 database
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
    Customer=Lender(name, borrow_amount, borrow_interest_rate, customer_id)
    return Customer

def main(adam_lend_amount, adam_lend_interest_rate):
    Lender=make_lender(adam_lend_amount, adam_lend_interest_rate,"Lender")
    return Lender #do we need to return this?




