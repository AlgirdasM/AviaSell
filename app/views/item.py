#!/usr/bin/env python3

from flask import render_template
from app import webapp
from app.models import *

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

        message = ""
        message += "Creating new item in category " + category_name + "\n"
        message += "title: " + title + "\n"
        message += "description: " + description + "\n"
        message += "location: " + location + "\n"
        message += "price: " + price + "\n"

        return message

    else:
        return "Create new item in category " + category_name


# Read item
@webapp.route('/category/<string:category_slug>/<string:item_name>/<int:item_id>')
def readItem(category_slug, item_name, item_id):
    item = ItemModel.getItem(item_id)
    user = UserModel.getUser(item.user_id)
    # Check if category exist, if not then 404
    q = CategoryModel.isThereCategory(category_slug)
    if q and item:
        return render_template('item.html', item = item, user = user, category_slug = category_slug)
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
