#!/usr/bin/env python3

from app import webapp
from flask import send_from_directory

# Serve uploaded pictures
@webapp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(webapp.config['UPLOAD_FOLDER'],
                               filename)