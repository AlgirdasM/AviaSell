#!/usr/bin/env python3

from flask import render_template
from app import webapp
from app.models import *
from flask import session as login_session

# Read main page
@webapp.route('/')
def mainIndex():
    categories = CategoryModel.getAll()
    catWithLatestItem = []

    for category in categories:
        catWithLatestItem.append((category, ItemModel.getLatestItem(category.id)))
    
    #for item, category in catWithLatestItem:
    #    print(item.title)
    #    print(category.name)

    return render_template('index.html', categories=catWithLatestItem, session=login_session)
