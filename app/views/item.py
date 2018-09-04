#!/usr/bin/env python3

from app import webapp
from app.controllers import *
from flask import render_template, request, url_for, redirect

# Create new item


@webapp.route('/item/create', methods=['GET', 'POST'])
def createItem():
    if request.method == 'POST':
        # Create and return created item
        data = ItemController.createItem(request.form, request.files)

        # If there is error, return error page
        if data.get('error'):
            return 'error page'

        # Redirect to item page
        return redirect(url_for('readItem',
                                category_slug=data['slug'],
                                item_name=data['item'].title,
                                item_id=data['item'].id))

    else:
        # Get all categories
        data = CategoryController.getAllCategories()
        return render_template('create.html', categories=data)


# Read item
@webapp.route('/category/<string:category_slug>/<string:item_name>/<int:item_id>')
def readItem(category_slug, item_name, item_id):
    # Get item data from ItemController
    data = ItemController.getItem(item_id, category_slug)

    return render_template('item.html',
                           item=data['item'],
                           user=data['user'],
                           category_slug=category_slug)


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
