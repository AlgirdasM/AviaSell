#!/usr/bin/env python3

from flask import render_template
from app import webapp
from app.models import *


# Read category page
@webapp.route('/category/<string:category_name>/')
def getCategory(category_name):
    # Check if category exist, if not then 404
    q = CategoryModel.isThereCategory(category_name)
    if q:
        # Filter by category ID and get items from database
        allItems = ItemModel.getAll(q.id)

        return render_template('category.html',
                               category_name=q.slug,
                               items=allItems)
    else:
        return render_template('404.html'), 404
