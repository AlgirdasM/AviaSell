#!/usr/bin/env python3

from flask import render_template
from app import webapp
from app.controllers import *

# Read category page
@webapp.route('/category/<string:category_slug>/', defaults={'page': 1})
@webapp.route('/category/<string:category_slug>/<int:page>')
def getCategoryPage(category_slug, page):
    login_session = AuthController.getSessionData()

    data = ItemController.getPageItems(category_slug, page)

    return render_template('category.html',
                           category_slug=category_slug,
                           items=data['items'],
                           category_name=data['category_name'],
                           pages=data['pageCount'],
                           current_page=page,
                           total_items=data['totalItems'],
                           session=login_session)