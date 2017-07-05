from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

errors = []

@app.route("/", methods=['POST'])
def login():
    '''checks input of the signup form and returns errors if incorrect
    or redirects to success page if everything is fine.'''

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    Name_Error = ' '
    Pass_Error = ' '
    Ver_Error = ' '
    Email_Error = ' '

    #Checks the username
    if len(username)<3 or len(username)>20 or username == '' or ' ' in username:
        Name_Error = "Please provide a valid username"

    #Checks the password
    if len(password)<3 or len(password)>20 or username == '' or ' ' in password:
        Pass_Error = "Please provide a valid password"

    #Checks the verified password
    if verify != password:
        Ver_Error = "Does not match your password"

    #Checks the email
    if len(email)<3 or len(email)>20 or username == '' or ' ' in email or email.count('@') != 1 or email.count('.') !=1:
        Email_Error = "Please provide a valid email"

    if Name_Error == ' ' and Pass_Error == ' ' and Ver_Error == ' ' and Email_Error == ' ':
        return render_template("success.html", username=username)
    else:
        return render_template('form.html', Name_Err=Name_Error, Pass_Err=Pass_Error,
                               Ver_Err=Ver_Error, Mail_Err=Email_Error,
                               username=username, email=email)

@app.route("/")
def index():
    '''renders the inital signup form'''
    return render_template('form.html', Name_Err='', Pass_Err='', Ver_Err='', Mail_Err='')



app.run()
