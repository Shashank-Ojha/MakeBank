# import the Flask class from the flask module
from flask import Flask, render_template, request
from wtforms import Form, BooleanField, TextField, PasswordField, validators
import search
import send_messages
from transfer import *
from pickle import dump, load


# create the application object
app = Flask(__name__)

class LenderForm(Form):
    amount = TextField('loanVal', [validators.Length(min=4, max=25)])
    rate = TextField('IRrange', [validators.Length(min=6, max=35)])


# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/index')
def index():
    return render_template('index.html')  # render a template

@app.route('/lend')
def lend():
    return render_template('lend.html')

@app.route('/lend', methods = ['POST'])
def chooseBorrow():
   if request.method == 'POST':
        amount = int(request.form['loanVal'])
        rate = float(request.form['IRrange'])
        database = search.get_borrowers(amount, rate)
        fout = open( 'database.pkl' , 'wb' )
        dump( database , fout , protocol = 2 )
        fout.close()

        #this will give you a list of burrowers
        return render_template("lenderSearch.html",
                                name1 = database[0].name,
                                amount1 = database[0].borrow_amount,
                                rate1 = database[0].borrow_interest_rate,
                                credit1 = round(database[0].credit_score,2),

                                name2 = database[1].name,
                                amount2 = database[1].borrow_amount,
                                rate2 = database[1].borrow_interest_rate,
                                credit2 = round(database[1].credit_score,2),

                                name3 = database[2].name,
                                amount3 = database[2].borrow_amount,
                                rate3 = database[2].borrow_interest_rate,
                                credit3 = round(database[2].credit_score,2)
                                )

@app.route('/borrow')
def borrow():
    return render_template('borrow.html')


@app.route('/borrowPosted')
def borrowPosted():
    return render_template('borrowPosted.html')

@app.route('/borrow', methods = ['POST'])
def chooseLender():
   if request.method == 'POST':
        amount = request.form['loanVal']
        rate = request.form['IRrange']
        #filename.main(amount, rate)
        return render_template("lenderSearch.html", amount = amount, rate = rate)

@app.route('/contact', methods = ['POST'])
def contact():
    if request.method == 'POST':
        body = "Hi, Hardik has requested to get in contact with you for your requested loan amount on MakeBank."
        phone = "+16309080289"
        send_messages.send_message(body, phone)
        transferIndex = str(request.form['person'])
        with open("client.txt", "wt") as f:
            f.write(transferIndex)
        return render_template('contact.html')

@app.route('/transfer')
def transferFromLender():
    database = load( open( 'database.pkl' , 'rb' ) )
    with open("client.txt", "rt") as f:
        transferIndex =  int(f.read())
    moneyLeft = transferMoney(database[transferIndex])
    print (moneyLeft)
    return render_template('transfer.html')





# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
