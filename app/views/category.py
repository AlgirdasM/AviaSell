#!/usr/bin/env python3

from flask import render_template
from app import webapp
from app.models import *
import math

# Read category page
@webapp.route('/category/<string:category_slug>')
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


@webapp.route('/category/<string:category_slug>/<int:page>')
def getCategoryPage(category_slug, page):
    # Check if category exist, if not then 404
    category = CategoryModel.getCategory(category_slug)
    if category:
        # How many items to display in one page?
        limitPerPage = 2
        # Get pages count
        pageCount = math.ceil(ItemModel.itemsInCatCount(category.id) / limitPerPage)
        # Filter by category ID and get items from database
        result = []
        items = ItemModel.getItemPage(category.id, page, limitPerPage)
        for item in items:
          result.append((item, UserModel.getUserEmail(item.user_id)))

        return render_template('category.html',
                               category_slug=category.slug,
                               items=result,
                               category_name=category.name,
                               pages=pageCount,
                               current_page=page)
    else:
        return render_template('404.html'), 404