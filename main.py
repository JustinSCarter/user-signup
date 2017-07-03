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

    #Checks the username
    if len(username)<3<20<len(username) or '' in username or ' ' in username:
        errors.insert(0,"Please provide a valid username")
    else:
        errors.insert(0,None)

    #Checks the password
    if len(password)<3<20<len(password) or '' in password or ' ' in password:
        errors.insert(1,"Please provide a valid password")
    else:
        errors.insert(1,None)

    #Checks the verified password
    if verify != password:
        errors.insert(2,"Does not match your password")
    else:
        errors.insert(2,None)

    #Checks the email
    if len(email)<3<20<len(email) or '' in email or ' ' in email or email.count('@') != 1 or email.count('.') !=1:
        errors.insert(3,"Please provide a valid email")
    else:
        errors.insert(3,None)

    if any in errors:
        return render_template('form.html', Name_Err=errors[0], Pass_Err=errors[1],
                               Ver_Err=errors[2], Mail_Err=errors[3],
                               username=username, email=email)
    else:
        return render_template("success.html", username=username)        

@app.route("/")
def index():
    '''renders the inital signup form'''
    return render_template('form.html', Name_Err='', Pass_Err='', Ver_Err='', Mail_Err='')



app.run()
