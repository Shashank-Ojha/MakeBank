import requests
import json

class Borrower(object):
    def __init__(self, name, borrow_amount, borrow_interest_rate, customer_id):
        self.name=name
        self.borrow_amount=borrow_amount
        self.borrow_interest_rate=borrow_interest_rate
        customer_url="http://api.reimaginebanking.com/customers/{}?key=dcd6272d8dab8b826b5c1376ac90af1b".format(customer_id)
        customer=requests.get(customer_url)
        customer=json.loads(customer.text)
        self.customer=customer  #capital one dictionary for get customers

#hardcoded for now to make a borrower named adam, who is already stored in captial 1 database
def make_borrower(name="Adam", borrow_amount, borrow_interest_rate):
    customers_url="http://api.reimaginebanking.com/customers?key=dcd6272d8dab8b826b5c1376ac90af1b"
    customers=requests.get(customers_url)
    customers=json.loads(customers.text)
    customer_id=None
    for customer in customers:
        if customer["first_name"]==name:
            customer_id=customer["_id"]
    # if customer_id==None:
        #do something
    Customer=Borrower(name,borrow_amount, interest_rate, customer_id)
    return Customer





