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

    if username == '' or if len(username)<3 or if len(username)>20 or if ' ' in username:
        error = "Please provide a valid username"
        else:
    if password == '' or if len(password)<3 or if len(password)>20 or if ' ' in password:
        error = "Please provide a valid password"
        else:
    if verify != password:
        error = "Does not match you password" 
        else:
    if email == '' or if len(email)<3 or if len(email)>20 or if ' ' in email or email.count('@') != 1 or email.count('.') !=1:
        error = "Please provide a valid email"
        else:

@app.route("/")
def index():
    '''renders the inital signup form'''
    return render_template('form.html')



app.run()
