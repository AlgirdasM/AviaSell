#!/usr/bin/env python3

from app import webapp
from flask import render_template
from flask import request, redirect, url_for
from app.controllers import *



# Read login page
@webapp.route('/login')
def login():
    # Set state
    state = AuthController.setState()
    return render_template('login.html', state=state)


@webapp.route('/gconnect', methods=['POST'])
def gconnect():
    # Get state
    reqstate = request.args.get('state')
    # Obtain authorization code
    code = request.data
    # Login using google login
    data = AuthController.loginGoogle(code, reqstate)
    return data


@webapp.route('/logout')
def logout():
    logged = AuthController.validateLogin()
    if not logged:
        return redirect(url_for('login'))
    
    data = AuthController.logout()
    if data['code'] == 200:
        # On success redirect to home page
        return redirect(url_for('mainIndex'))
    else:
        # On error display error page
        message = data['message']
        code = data['code']
        return render_template('error.html', message=message), code