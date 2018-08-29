#!/usr/bin/env python3

from flask import render_template
from app import webapp
from app.models import *

# Read category page
@webapp.route('/category/<string:category_name>/')
def getCategory(category_name):
    q = CategoryModel.isThereCategory(category_name)
    if q:
        return render_template('category.html')
    else:
        return render_template('404.html'), 404