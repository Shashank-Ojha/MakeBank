import requests
import json
from borrowers.py import *

#focus on lender
#search by only amount, not interest rate

def sort_borrowers(lender_amount, borrowers):
    #borrowers of type Borrower
    #want a lower match score
    borrowers_and_match_score={}
    for borrower in borrowers:
        diff=abs(borrower.borrow_amount-lender_amount)
        borrowers_and_match_score[diff]=borrower
    #sort backwards becuase you want lower difference
    match_scores_sorted=sorted(d.keys())[::-1]
    sorted_borrowers=[]
    for match_score in match_scores_sorted:
        borrower=borrowers_and_match_score[match_score]
        sorted_borrowers.append(borrower)
    return sorted_borrowers
