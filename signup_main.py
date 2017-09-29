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
    password = request.form['password']
    verify_password = request.form['verify']

    name_error = ''
    pass_error = ''

    if user_name == '':
        name_error = 'Please enter a user name.'
    elif len(user_name)<3 or len(user_name)>20:
        name_error = 'User name must be 3 - 20 characters long.'
        user_name = ''
    elif " " in user_name:
        name_error = 'Username cannot contain spaces.'
        user_name = ''

    if password == '':
        pass_error = 'Please enter a password.'
    elif len(password)<3 or len(password)>10:
        pass_error = 'Password must be 3 - 10 characters long.'
        password = ''
        verify_password = ''
    elif " " in password:
        pass_error = 'Password cannot contain spaces.'
        password = ''
        verify_password = ''
    elif verify_password != password:
        pass_error = 'Passwords do not match.'
        verify_password = ''
        
    if name_error == '' and pass_error == '':
        return render_template('success.html')
    else:
        return render_template('form_fields.html',name=user_name, password=password,verify_password=verify_password,name_error=name_error,pass_error=pass_error)

app.run()