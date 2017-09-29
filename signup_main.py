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

    if user_name == '':
        name_error = 'Please enter a user name.'
        return render_template('form_fields.html',name=user_name,name_error=name_error)
    elif len(user_name)<3 or len(user_name)>20:
        name_error = 'User name must be between 3 & 20 characters.'
        user_name = ''
        return render_template('form_fields.html',name=user_name,name_error=name_error)
    elif " " in user_name:
        name_error = 'Username cannot contain spaces.'
        user_name = ''
        return render_template('form_fields.html',name=user_name,name_error=name_error)

    if password == '':
        pass_error = 'Please enter a password.'
        return render_template('form_fields.html',password=password,pass_error=pass_error)
    elif len(password)<3 or len(password)>10:
        pass_error = 'Password must be 3 - 10 characters long.'
        password = ''
        return render_template('form_fields.html',password=password,pass_error=pass_error)
    elif " " in password:
        pass_error = 'Password cannot contain spaces.'
        password = ''
        return render_template('form_fields.html',password=password,pass_error=pass_error)
    

    return render_template('success.html')


app.run()