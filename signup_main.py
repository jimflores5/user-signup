from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True
 
@app.route("/")
def index():
    return render_template('form_fields.html')

@app.route("/", methods=['POST'])
def user_name_valid():
    user_name = request.form['username']

    if len(user_name)<3 or len(user_name)>20:
        return render_template('invalid_username.html')

    return render_template('success.html')


app.run()