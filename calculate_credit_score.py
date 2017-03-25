import requests
import json

#merchant 1(grocery): "57cf75cea73e494d8675ec4b #good
#merchant 2(clothes): 57cf75cea73e494d8675ec50  #ok 
#merchant 3(personal): 57cf75cea73e494d8675ec51 #worst
def get_purchase_by_account(account_id):
    purchase_url="http://api.reimaginebanking.com/accounts/{}/purchases?key=dcd6272d8dab8b826b5c1376ac90af1b".format(account_id)
    purchases=requests.get(purchase_url)
    purchases=json.loads(purchases.text)
    l=[]
    for purchase in purchases:
        purchase_amount=purchase["amount"]
        l.append(purchase_amount)
    return l

def get_purchase_amounts():
    account_url="http://api.reimaginebanking.com/accounts?key=dcd6272d8dab8b826b5c1376ac90af1b"
    all_accounts=requests.get(account_url)
    all_accounts=json.loads(all_accounts.text)
    acc=[] #list of lists. [[clothes], [groceries], [personal]]
    for account in all_accounts:
        account_id=account["_id"]
        #do something with this
        l=get_purchase_by_account(account_id)
        clothes=l[0:12]
        groceries=l[12:-5]
        personal=l[-5:]
        acc.append(clothes)
        acc.append(groceries)
        acc.append(personal)
        print(acc) #do something with this acc
    return l

(get_purchase_amounts())

