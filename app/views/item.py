#!/usr/bin/env python3

import os
from flask import render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from app import webapp
from app.models import *
import uuid

UPLOAD_FOLDER = '/vagrant/catalog/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
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
@webapp.route('/category/<string:category_slug>/create', methods=['GET', 'POST'])
def createItem(category_slug):
    category = CategoryModel.isThereCategory(category_slug)
    user_id = '1';
    item = {}

    if request.method == 'POST':
        # Check if all data is available
        if request.form.get('title') and\
           request.form.get('description') and\
           request.form.get('location') and\
           request.form.get('price'):
            item['title'] = request.form['title']
            item['description'] = request.form['description']
            item['location'] = request.form['location']
            item['price'] = request.form['price']
        else:
            return "Error"

        # Check if the post request has the picture part
        if 'itemPicture' not in request.files:
            return "We need itemPicture!"
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
            item['picture'] = randomFileName
            file.save(os.path.join(
                webapp.config['UPLOAD_FOLDER'], randomFileName))
            # redirect(url_for('uploaded_file',
            #                       filename=filename))


        return ItemModel.createItem(item, category.id, user_id)

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
