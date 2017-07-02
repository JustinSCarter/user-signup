from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    error_list = ()

    if username == '' or if len(username) < 3 or if len(username) > 20 or if ' ' in username:
        append.error_list("Please provide a valid username")
        else:
            append.eror_list(" ")
    elif password == '' or if len(password) < 3 or if len(password) > 20 or if ' ' in password:
        append.error_list("Please provide a valid password")
        else:
            append.eror_list(" ")
    elif verify != password:
        append.error_list("Does not match you password")
        else:
            append.eror_list(" ")
    elif email == '' or if len(email) < 3 or if len(email) > 20 or if ' ' in email or email.count('@') != 1 or email.count('.') !=1:
        append.error_list("Please provide a valid email")
        else:
            append.eror_list(" ")

    if error_list = ( , , , )
        #redirect to successful page
        else:
            #render form with errors
    
@app.route("/")
def index():
    '''renders the inital signup form'''
    return render_template('form.html')



app.run()
