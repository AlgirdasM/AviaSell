#!/usr/bin/env python3

from flask import render_template
from app import webapp
from app.models import *


# Read category page
@webapp.route('/category/<string:category_slug>/')
def getCategory(category_slug):
    # Check if category exist, if not then 404
    category = CategoryModel.getCategory(category_slug)
    if category:
        # Filter by category ID and get items from database
        allItems = ItemModel.getAll(category.id)

        return render_template('category.html',
                               category_slug=category.slug,
                               items=allItems,
                               category_name=category.name)
    else:
        return render_template('404.html'), 404
