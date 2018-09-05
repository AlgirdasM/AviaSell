#!/usr/bin/env python3

from flask import render_template
from app import webapp

# Display errors using template
@webapp.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message=e), 404