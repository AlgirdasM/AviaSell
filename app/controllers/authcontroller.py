#!/usr/bin/env python3

import random, string, httplib2, json, requests
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from app.models import *
from flask import session as login_session
from flask import make_response

with open('app/config/gclient_secret.json') as f:
    CLIENT_ID = json.load(f)['web']['client_id']

class AuthController():
    # Return session data
    def getSessionData():
        return login_session

    def setState():
        # Generate random 32 char state
        state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                        for x in range(32))
        # Add state to login session
        login_session['state'] = state
        return login_session['state']

    def validateState(reqstate):
        # If state is valid return true
        return reqstate == login_session['state']

    def loginGoogle(code, reqstate):
        # If state is not valid return error
        if not AuthController.validateState(reqstate):
            response = make_response(json.dumps('Invalid state parameter.'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response

        try:
            # Upgrade the authorization code into a credentials object
            oauth_flow = flow_from_clientsecrets(
                webapp.config['GOOGLE_JSON'], scope='')
            oauth_flow.redirect_uri = 'postmessage'
            credentials = oauth_flow.step2_exchange(code)
        except FlowExchangeError:
            response = make_response(
                json.dumps('Failed to upgrade the authorization code.'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response

        # Check that the access token is valid.
        access_token = credentials.access_token
        url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
               % access_token)
        h = httplib2.Http()
        result = json.loads(h.request(url, 'GET')[1].decode('utf-8'))

        # If there was an error in the access token info, abort.
        if result.get('error') is not None:
            response = make_response(json.dumps(result.get('error')), 500)
            response.headers['Content-Type'] = 'application/json'
            return response

        # Verify that the access token is used for the intended user.
        gplus_id = credentials.id_token['sub']
        if result['user_id'] != gplus_id:
            response = make_response(
                json.dumps(
                    "Token's user ID doesn't match given user ID."), 401)
            response.headers['Content-Type'] = 'application/json'
            return response

        # Verify that the access token is valid for this app.
        if result['issued_to'] != CLIENT_ID:
            response = make_response(
                json.dumps("Token's client ID does not match app's."), 401)
            print("Tokens client ID does not match apps.")
            response.headers['Content-Type'] = 'application/json'
            return response

        stored_access_token = login_session.get('access_token')
        stored_gplus_id = login_session.get('gplus_id')
        if stored_access_token is not None and gplus_id == stored_gplus_id:
            response = make_response(
                json.dumps('Current user is already connected.'), 200)
            response.headers['Content-Type'] = 'application/json'
            return response

        # Store the access token in the session for later use.
        login_session['access_token'] = credentials.access_token
        login_session['gplus_id'] = gplus_id

        # Get user info
        userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        params = {'access_token': credentials.access_token, 'alt': 'json'}
        answer = requests.get(userinfo_url, params=params)

        data = answer.json()

        login_session['username'] = data['name']
        login_session['picture'] = data['picture']
        login_session['email'] = data['email']

        # ADD PROVIDER TO LOGIN SESSION
        login_session['provider'] = 'google'

        # See if user exists, if it doesn't make a new one
        user_id = UserModel.getUserID(data["email"])
        if not user_id:
            user_id = UserModel.createUser(login_session)
        login_session['user_id'] = user_id

        output = ''
        output += '<h1>Login Successful!</h1>'
        output += '<img class="avatar" src="'
        output += login_session['picture']
        output += '" >'
        output += '<p>Welcome, '
        output += login_session['username']
        output += '</p>'

        return output

    def logout():
        # Only disconnect a connected user.
        access_token = login_session.get('access_token')
       
       # Clear login session
        login_session.clear()

        if access_token is None:
            response = make_response(
                json.dumps('Current user not connected.'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response
        
        url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
        h = httplib2.Http()
        result = h.request(url, 'GET')[0]
        
        if result['status'] == '200':
            # Return success
            return 'success'
        else:
            response = make_response(json.dumps('Failed to revoke token for given user.', 400))
            response.headers['Content-Type'] = 'application/json'
            return response