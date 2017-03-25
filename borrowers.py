import requests
import json

class Borrower(object):
    borrowers=[]
    def __init__(self, name, borrow_amount, borrow_interest_rate, customer_id):
        self.name=name
        self.borrow_amount=borrow_amount
        self.borrow_interest_rate=borrow_interest_rate
        customer_url="http://api.reimaginebanking.com/customers/{}?key=dcd6272d8dab8b826b5c1376ac90af1b".format(customer_id)
        customer=requests.get(customer_url)
        customer=json.loads(customer.text)
        self.customer=customer  #capital one dictionary for get customers

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
    Customer=Borrower(name,borrow_amount, interest_rate, customer_id)
    return Customer
    
adam_borrow_amount=0 #wait for input
adam_borrow_interest_rate=0 #wait for input
Adam=make_borrower(adam_borrow_amount, adam_borrow_interest_rate,"Adam")
billy_borrow_amount=100
billy_interest_rate=2
Billy=make_borrower(billy_borrow_amount, billy_interest_rate, "Billy")
carlisle_borrow_amount=600
carlisle_interest_rate=2
Carlisle=make_borrower(carlisle_borrow_amount, carlisle_interest_rate, "Carlisle")
borrowers=[Adam, Billy, Carlisle]
    






