#!/usr/bin/env python3

from app import webapp
from app.controllers import *
from flask import render_template, request, url_for, redirect


# Read item
@webapp.route('/category/<string:category_slug>/<string:item_name>/<int:item_id>')
def readItem(category_slug, item_name, item_id):
    # Validate category slug
    validSlug = CategoryController.validateSlug(category_slug)
    if not validSlug:
        message = '404 - Category Not Found'
        return render_template('error.html', message=message), 404

    # Get item data from ItemController
    data = ItemController.getItem(item_id, item_name)
    # If we don't have item return error
    if not data:
        message = '404 - Item Not Found'
        return render_template('error.html', message=message), 404

    return render_template('item.html',
                           item=data['item'],
                           user=data['user'],
                           category_slug=category_slug)


# Create new item
@webapp.route('/item/create', methods=['GET', 'POST'])
def createItem():
    logged = AuthController.validateLogin()
    if not logged:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Create and return created item
        data = ItemController.createItem(request.form, request.files)

        # If there is error, return error page
        if data.get('error'):
            message = data['error']
            return render_template('error.html', message=message), 400

        # Redirect to item page
        return redirect(url_for('readItem',
                                category_slug=data['slug'],
                                item_name=data['item'].title,
                                item_id=data['item'].id))

    else:
        # Get all categories
        data = CategoryController.getAllCategories()
        return render_template('create.html', categories=data)


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
@webapp.route('/item/delete/<int:item_id>', methods=['GET', 'POST'])
def deleteItem(item_id):
    logged = AuthController.validateLogin()
    if not logged:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        data = ItemController.deleteItem(item_id)

        if data['code'] == 200:
            # flash message because we need to inform that item is deleted successfully
            return 'Item is deleted'
        else:
            message = data['message']
            code = data['code']
            return render_template('error.html', message=message), code
    else:
        data = ItemController.getItemByID(item_id)
        
        if not data:
            message = 'Item not found'
            code = 404
            return render_template('error.html', message=message), code

        return render_template('delete.html', item=data)
