#!/usr/bin/env python3

import os
from flask import render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from app import webapp
from app.models import *
import uuid

UPLOAD_FOLDER = '/vagrant/catalog/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])
webapp.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
webapp.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024


def idGenerator():
    return str(uuid.uuid4())


def getExtension(filename):
    return filename.split('.')[-1]


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Create new item
@webapp.route('/category/<string:category_name>/create', methods=['GET', 'POST'])
def createItem(category_name):
    if request.method == 'POST':
        if request.form.get('title'):
            title = request.form['title']
        else:
            return "Error, missing title argument"

        if request.form.get('description'):
            description = request.form['description']
        else:
            return "Error, missing description argument"

        if request.form.get('location'):
            location = request.form['location']
        else:
            return "Error, missing location argument"

        if request.form.get('price'):
            price = request.form['price']
        else:
            return "Error, missing price argument"

        # check if the post request has the file part
        if 'itemPicture' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['itemPicture']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # generate random new filename
            randomFileName = idGenerator() + "." + getExtension(filename)
            file.save(os.path.join(
                webapp.config['UPLOAD_FOLDER'], randomFileName))
            # redirect(url_for('uploaded_file',
            #                       filename=filename))

        message = ""
        message += "Creating new item in category " + category_name + "\n"
        message += "title: " + title + "\n"
        message += "description: " + description + "\n"
        message += "location: " + location + "\n"
        message += "price: " + price + "\n"
        message += "image:" + randomFileName

        return message

    else:
        return render_template('create.html')


# Serve uploaded pictures
@webapp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(webapp.config['UPLOAD_FOLDER'],
                               filename)


# Read item
@webapp.route('/category/<string:category_slug>/<string:item_name>/<int:item_id>')
def readItem(category_slug, item_name, item_id):
    item = ItemModel.getItem(item_id)
    user = UserModel.getUser(item.user_id)
    # Check if category exist, if not then 404
    q = CategoryModel.isThereCategory(category_slug)
    if q and item:
        return render_template('item.html', item=item, user=user, category_slug=category_slug)
    else:
        return render_template('404.html')


# Update item
@webapp.route('/category/<string:category_name>/<int:item_id>/update', methods=['GET', 'POST'])
def updateItem(category_name, item_id):
    if request.method == 'POST':
        message = ""

        if request.form.get('title'):
            title = request.form['title']
            message += "title: " + title + "\n"

        if request.form.get('description'):
            description = request.form['description']
            message += "description: " + description + "\n"

        if request.form.get('location'):
            location = request.form['location']
            message += "location: " + location + "\n"

        if request.form.get('price'):
            price = request.form['price']
            message += "price: " + price + "\n"

        message += "Updating item with id " + \
            str(item_id) + " in category " + category_name

        return message
    else:
        return "Edit: item with id: " + str(item_id) + " in category " + category_name


# Delete item
@webapp.route('/category/<string:category_name>/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(category_name, item_id):
    if request.method == 'POST':
        return "Deleting item id: " + str(item_id)
    else:
        return "Edit: item with id: " + str(item_id) + " in category " + category_name
