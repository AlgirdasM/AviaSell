#!/usr/bin/env python3

from app.models import *
import math
from app import webapp
from flask import session as login_session
from app.controllers.uploadcontroller import UploadController

class ItemController():
    # Get items for given category and page
    def getPageItems(category_slug, page):
        try:
            # How many items to display in one page?
            limitPerPage = int(webapp.config['ITEMS_PER_PAGE'])

            # Create object to store data
            result = {}

            # Get category information using slug
            category = CategoryModel.getCategoryBySlug(category_slug)
            result['category_name'] = category.name

            # Get total items
            totalItems = ItemModel.itemsInCategoryCount(category.id)
            result['totalItems'] = totalItems

            # Count how many there are pages
            pageCount = math.ceil(totalItems / limitPerPage)
            result['pageCount'] = pageCount

            # Filter by category ID and get items from database
            result['items'] = []
            items = ItemModel.getItemPage(category.id, page, limitPerPage)
            for item in items:
                result['items'].append(
                    (item, UserModel.getUserEmail(item.user_id)))

            return result
        # if we got exception, return false
        except:
            return False

    def getItemByID(item_id):
        try:
            # Get item data by id
            item = ItemModel.getItem(item_id)

            return item
        except:
            # If error return false
            return False

    def getItem(item_id, item_name):
        try:
            # Create object to store data
            result = {}

            # Get item data
            item = ItemModel.getItem(item_id)
            result['item'] = item

            # Validate item name, if it doesnt match return False
            if item.title != item_name:
                return False

            # Get user data
            user = UserModel.getUser(item.user_id)
            result['user'] = user

            return result
        except:
            # If error return false
            return False

    def createItem(data, file):
        # Create object to store data
        result = {}

        # Validate data, it must not be empty
        if not data.get('title'):
            result['error'] = 'Title is required'
        if not data.get('description'):
            result['error'] = 'Description is required'
        if not data.get('location'):
            result['error'] = 'Location is required'
        if not data.get('price'):
            result['error'] = 'Price is required'
        if not data.get('category_id'):
            result['error'] = 'Category id is required'

        if result.get('error'):
            return result

        # Get logged in user id
        user_id = str(login_session['user_id'])

        # Upload picture to our server and return unique filename
        picture = UploadController.uploadFile(file, user_id)

        # Create item and return it
        item = ItemModel.createItem(data, picture, user_id)
        result['item'] = item

        # Get category slug
        categorySlug = CategoryModel.getCategorySlug(item.category_id)
        result['slug'] = categorySlug

        return result

    def updateItem(item_id, data, file):
        # Create object to store data
        response = {}

        # Get item data
        item = ItemModel.getItem(item_id)

        # Get user id
        user_id = str(login_session['user_id'])

        # If item not found return 404 with message
        if not item:
            response['message'] = 'Item not found'
            response['code'] = 404
            return response

        # Get request data
        if data.get('title'):
            item.title = data['title']
        if data.get('description'):
            item.description = data['description']
        if data.get('location'):
            item.location = data['location']
        if data.get('price'):
            item.price = data['price']
        if data.get('category_id'):
            item.category_id = data['category_id']
        if file.get('itemPicture'):
            picture = UploadController.uploadFile(file, user_id)
            item.picture = picture

        # Update item and return it
        itemUpdate = ItemModel.updateItem(item)

        # Get category slug
        slug = CategoryModel.getCategorySlug(itemUpdate.category_id)

        if itemUpdate:
            # Return response code 200 if everything is ok
            response['item'] = itemUpdate
            response['slug'] = slug
            response['code'] = 200
            return response
        else:
            response['message'] = 'Something went wrong... Item is not updated.'
            response['code'] = 304
            return response

    def deleteItem(item_id):
        # Create object to store data
        response = {}

        # Get item data
        item = ItemModel.getItem(item_id)

        # Get user id
        user_id = login_session['user_id']
        
        # If item not found return 404
        if not item:
            response['message'] = 'Item not found'
            response['code'] = 404
            return response

        # check if user is authorized to delete this item
        if item.user_id != user_id:
            response['message'] = 'You are not authorized to delete this item.'
            response['code'] = 403
            return response

        #delete item and return response code 200
        delete_item = ItemModel.deleteItem(item_id)
        slug = CategoryModel.getCategorySlug(delete_item.category_id)

        if delete_item:
            response['slug'] = slug
            response['code'] = 200
            return response
        else:
            response['message'] = 'Something went wrong... Item is not deleted.'
            response['code'] = 500
            return response