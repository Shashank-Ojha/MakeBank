# import the Flask class from the flask module
from flask import Flask, render_template, request
from wtforms import Form, BooleanField, TextField, PasswordField, validators
#import pythonfiles(no .py)


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
        amount = request.form['loanVal']
        rate = request.form['IRrange']
        #filename.main(amount, rate)
        #this will give search results
        return render_template("lenderSearch.html", amount = amount, rate = rate)

@app.route('/borrow')
def borrow():
    return render_template('borrow.html')

@app.route('/borrow', methods = ['POST'])
def chooseLender():
   if request.method == 'POST':
        amount = request.form['loanVal']
        rate = request.form['IRrange']
        #filename.main(amount, rate)
        #this will give search results
        return render_template("lenderSearch.html", amount = amount, rate = rate)



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
