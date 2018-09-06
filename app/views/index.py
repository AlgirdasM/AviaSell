#!/usr/bin/env python3

from flask import render_template
from app import webapp
from app.controllers import *


# Render index page
@webapp.route('/')
def mainIndex():
    # Get categories with latest item
    categories = CategoryController.categoriesWithLatestItem()

    # Get session data
    login_session = AuthController.getSessionData()
    return render_template('index.html',
                           categories=categories,
                           session=login_session)
