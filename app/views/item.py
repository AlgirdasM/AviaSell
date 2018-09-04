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
    # Validate if user loged, if not redirect to login page
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
@webapp.route('/item/update/<int:item_id>', methods=['GET', 'POST'])
def updateItem(item_id):
    # Validate if user loged, if not redirect to login page
    logged = AuthController.validateLogin()
    if not logged:
        return redirect(url_for('readItem'))
    
    if request.method == 'POST':
        data = ItemController.updateItem(item_id, request.form, request.files)
        if data['code'] == 200:
            return redirect(url_for('readItem',
                                    category_slug=data['slug'],
                                    item_name=data['item'].title,
                                    item_id=data['item'].id))
        else:
            message = data['message']
            code = data['code']
            return render_template('error.html', message=message), 304
    else:
        data = ItemController.getItemByID(item_id)
        categories = CategoryController.getAllCategories()
        return render_template('update.html', item=data, categories=categories)


# Delete item
@webapp.route('/item/delete/<int:item_id>', methods=['GET', 'POST'])
def deleteItem(item_id):
    # Validate if user loged, if not redirect to login page
    logged = AuthController.validateLogin()
    if not logged:
        return redirect(url_for('readItem'))

    if request.method == 'POST':
        data = ItemController.deleteItem(item_id)

        if data['code'] == 200:
            # Redirect to home category page and
            # flash message because we need to inform
            # that item is deleted successfully
            return redirect(url_for('getCategoryPage',
                        category_slug=data['slug']))
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
