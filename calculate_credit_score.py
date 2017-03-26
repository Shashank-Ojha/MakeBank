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
    users = []
    for account in all_accounts:
        acc=[] #list of lists. [[clothes], [groceries], [personal]]
        account_id=account["_id"]
        #do something with this
        l=get_purchase_by_account(account_id)
        clothes=l[0:12]
        groceries=l[12:-6]
        personal=l[-6:]
        acc.append(clothes)
        acc.append(groceries)
        acc.append(personal)
        users.append(acc)
    return users

def overlayPurchases(l):
    overlayed = []
    for i in range(len(l[0])): #syncs to monthly basis ie clothes
        overlayed.append(l[0][i])
        i1 = (len(l[1])//len(l[0]))*i
        i2 = i1 + (len(l[1])//len(l[0]))
        overlayed[i] += sum(l[1][i1:i2])
        if i % 2==0:
            overlayed[i] += l[2][i//2]
    return overlayed

def getScore():
    x = get_purchase_amounts()
    stds = []
    for i in x[:-1]:
        w = overlayPurchases(i)
        mean  = sum(w)/len(w)
        sumOfSquares = 0
        for j in w:
            sumOfSquares += (j-mean)**2
        
        std = 400-(sumOfSquares/len(w))**0.5
        stds.append(int(std))
    return stds
print(getScore())
