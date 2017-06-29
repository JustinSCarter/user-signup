from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def login():
    '''renders the inital signup form'''
    return render_template('form.html')

app.run()
