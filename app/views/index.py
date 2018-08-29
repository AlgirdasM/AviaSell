#!/usr/bin/env python3

from flask import render_template
from app import webapp
from app.models import *


# Read main page
@webapp.route('/')
def main():
    return render_template('index.html', categories=CategoryModel.getAll())
