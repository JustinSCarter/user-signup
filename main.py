from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


errors = ('nope')

@app.route("/", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    # if username == '' or if len(username) < 3 or if len(username) > 20 or if ' ' in username:
    #     errors.insert(0,"Please provide a valid username")
    # if password == '' or if len(password) < 3 or if len(password) > 20 or if ' ' in password:
    #     errors.insert(1,"Please provide a valid password")
    # if verify != password:
    #     errors.insert(2,"Does not match your password")
    # if email == '' or if len(email) < 3 or if len(email) > 20 or if ' ' in email or email.count('@') != 1 or email.count('.') !=1:
    #     errors.insert(3,"Please provide a valid email")

    if any(errors):
        return render_template('form.html', Name_Err=errors[0], Pass_Err=errors[1], Ver_Err=errors[2], Mail_Err=errors[3], username=username, email=email)
    else:
        return render_template("success.html", username=username)

@app.route("/")
def index():
    '''renders the inital signup form'''
    return render_template('form.html', Name_Err='', Pass_Err='', Ver_Err='', Mail_Err='')



app.run()
