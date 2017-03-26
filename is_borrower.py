import requests
import json
from calculate_credit_score import *

class Borrower(object):
    def __init__(self, name, borrow_amount, borrow_interest_rate, customer_id):
        self.name=name
        self.borrow_amount=borrow_amount
        self.borrow_interest_rate=borrow_interest_rate
        customer_url="http://api.reimaginebanking.com/customers/{}?key=dcd6272d8dab8b826b5c1376ac90af1b".format(customer_id)
        customer=requests.get(customer_url)
        customer=json.loads(customer.text)
        self.customer=customer  #capital one dictionary for get customers
        if name=="Sasha":
            self.credit_score=224.95
        if name=="Teg":
            self.credit_score=131.37
        if name=="Rihanna":
            self.credit_score=112.15
        if name=="Adam":
            self.credit_score=get_score()[0]
        if name=="Billy":
            self.credit_score=get_score()[1]
        if name=="Carlisle":
            self.credit_score=get_score()[2]
            
#hardcoded for now to make a borrower named adam, who is already stored in captial 1 database
def make_borrower(borrow_amount, borrow_interest_rate, name):
    customers_url="http://api.reimaginebanking.com/customers?key=dcd6272d8dab8b826b5c1376ac90af1b"
    customers=requests.get(customers_url)
    customers=json.loads(customers.text)
    customer_id=None
    for customer in customers:
        if customer["first_name"]==name:
            customer_id=customer["_id"]
    # if customer_id==None:
        #do something
    Customer=Borrower(name, borrow_amount, borrow_interest_rate, customer_id)
    return Customer

def main():
    adam_borrow_amount=200
    adam_borrow_interest_rate=2
    Adam=make_borrower(adam_borrow_amount, adam_borrow_interest_rate,"Adam")
    billy_borrow_amount=100
    billy_interest_rate=2
    Billy=make_borrower(billy_borrow_amount, billy_interest_rate, "Billy")
    carlisle_borrow_amount=600
    carlisle_interest_rate=3
    Carlisle=make_borrower(carlisle_borrow_amount, carlisle_interest_rate, "Carlisle")
    sasha_borrow_amount=250
    sasha_interest_rate=1
    Sasha=make_borrower(sasha_borrow_amount, sasha_interest_rate, "Sasha")
    rihanna_borrow_amount=400
    rihanna_interest_rate=4
    Rihanna=make_borrower(rihanna_borrow_amount, rihanna_interest_rate, "Rihanna")
    teg_borrow_amount=800
    teg_interest_rate=5
    Teg=make_borrower(teg_borrow_amount, teg_interest_rate, "Teg")
    borrowers=[Adam, Billy, Carlisle, Sasha, Rihanna, Teg] #all of type Borrowes
    return borrowers






