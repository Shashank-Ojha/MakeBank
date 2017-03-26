import requests
import json
from is_borrower import *

#focus on lender
#search by only amount, not interest rate

def sort_borrowers(lender_amount, borrowers):
    #borrowers of type Borrower
    #want a lower match score

    borrowers_and_match_score={}
    for borrower in borrowers:
        interest_rate_score=0
        if lender_amount==0.5 and not(0<=borrower.borrower_interest_rate
        or borrower.borrower_interest_rate<1):
            interest_rate_score=50
        if lender_amount==1.5 and not(1<=borrower.borrower_interest_rate
        or borrower.borrower_interest_rate<2):
            interest_rate_score=50
        if lender_amount==2.5 and not(2<=borrower.borrower_interest_rate
        or borrower.borrower_interest_rate<3):
            interest_rate_score=50
        if lender_amount==3.5 and not(3<=borrower.borrower_interest_rate):
            interest_rate_score=50
        diff=abs(borrower.borrow_amount-lender_amount)+(400-borrower.credit_score)*.4+interest_rate_score
        borrowers_and_match_score[diff]=borrower
    #sort backwards becuase you want lower difference
    match_scores_sorted=sorted(borrowers_and_match_score.keys())
    sorted_borrowers=[]
    for match_score in match_scores_sorted:
        borrower=borrowers_and_match_score[match_score]
        sorted_borrowers.append(borrower)
    return sorted_borrowers

def get_borrowers(lender_amount, lender_interest_rate):
    borrowers=main()
    return sort_borrowers(lender_amount, borrowers)[:3]
