#!/usr/bin/env python3

import os
from flask import render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from app import webapp
from app.models import *
import uuid
from flask import session as login_session

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
@webapp.route('/item/create', methods=['GET', 'POST'])
def createItem():
    if request.method == 'POST':
        # Create item to store information
        item = {}
        user_id = str(login_session['user_id'])
        # Check if all required data is available in post
        if request.form.get('title') and\
           request.form.get('description') and\
           request.form.get('location') and\
           request.form.get('price') and\
           request.form.get('category'):
            item['title'] = request.form['title']
            item['description'] = request.form['description']
            item['location'] = request.form['location']
            item['price'] = request.form['price']
            item['category_id'] = request.form['category']
        else:
            return 'Error'

        # Check if the post request has the picture part
        if 'itemPicture' in request.files:
            file = request.files['itemPicture']
            # if file exist and it's allowed
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # generate random new filename
                # user_id-randomstring.ext
                randomFileName = user_id + '-' + idGenerator() + '.' + getExtension(filename)
                item['picture'] = randomFileName
                file.save(os.path.join(
                    webapp.config['UPLOAD_FOLDER'], randomFileName))
        else:
            # If no picture is selected submit empty string
            item['picture'] = ''
        
        # Create and return created item
        created = ItemModel.createItem(item, user_id)
        # Get category slug using category_id
        categorySlug = CategoryModel.getCategorySlug(created.category_id)
        
        #redirect to item page
        return redirect(url_for('readItem', category_slug = categorySlug, item_name=created.title, item_id=created.id))

    else:
        categories = CategoryModel.getAll()
        return render_template('create.html', categories=categories)


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
    category = CategoryModel.getCategory(category_slug)
    if category and item:
        return render_template('item.html', item=item, user=user, category_slug=category_slug)
    else:
        return render_template('404.html')


# Update item
@webapp.route('/category/<string:category_name>/<int:item_id>/update', methods=['GET', 'POST'])
def updateItem(category_name, item_id):
    if request.method == 'POST':
        message = ''

        if request.form.get('title'):
            title = request.form['title']
            message += 'title: ' + title + '\n'

        if request.form.get('description'):
            description = request.form['description']
            message += 'description: ' + description + '\n'

        if request.form.get('location'):
            location = request.form['location']
            message += 'location: ' + location + '\n'

        if request.form.get('price'):
            price = request.form['price']
            message += 'price: ' + price + '\n'

        message += 'Updating item with id ' + \
            str(item_id) + ' in category ' + category_name

        return message
    else:
        return 'Edit: item with id: ' + str(item_id) + ' in category ' + category_name


# Delete item
@webapp.route('/category/<string:category_name>/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(category_name, item_id):
    if request.method == 'POST':
        return 'Deleting item id: ' + str(item_id)
    else:
        return 'Edit: item with id: ' + str(item_id) + ' in category ' + category_name
