#!/usr/bin/env python3

from flask import render_template
from app import webapp


# Read login page
@webapp.route('/login')
def login():
    return "This is login page"