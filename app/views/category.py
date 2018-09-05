#!/usr/bin/env python3

from flask import render_template
from app import webapp
from app.controllers import *

# Read category page, if no page, default is 1
@webapp.route('/category/<string:category_slug>/', defaults={'page': 1})
@webapp.route('/category/<string:category_slug>/<int:page>')
def getCategoryPage(category_slug, page):
    # Get loggin session data
    login_session = AuthController.getSessionData()
    # Get items per page
    data = ItemController.getPageItems(category_slug, page)
    # If there is no data return 404
    if not data:
      message = '404 - Category Not Found'
      return render_template('error.html', message=message), 404

    # We got data, display it
    return render_template('category.html',
                           category_slug=category_slug,
                           items=data['items'],
                           category_name=data['category_name'],
                           pages=data['pageCount'],
                           current_page=page,
                           total_items=data['totalItems'],
                           session=login_session)