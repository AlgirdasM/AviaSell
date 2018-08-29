#!/usr/bin/env python3

from flask import render_template
from app import webapp


# Read category page
@webapp.route('/category/<string:category_name>/')
def category(category_name):
    return "Category page"