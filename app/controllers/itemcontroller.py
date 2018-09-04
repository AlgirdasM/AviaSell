#!/usr/bin/env python3

from app.models import *
import math
from app import webapp
from flask import session as login_session
from app.controllers.uploadcontroller import UploadController

class ItemController():
    # Get items for given category and page
    def getPageItems(category_slug, page):
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

    def getItem(item_id, category_slug):
        # Create object to store data
        result = {}

        # Get item data
        item = ItemModel.getItem(item_id)
        result['item'] = item

        # Get user data
        user = UserModel.getUser(item.user_id)
        result['user'] = user

        return result

    def createItem(data, file):
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
        picture = UploadController.uploadFile(file, user_id)

        item = ItemModel.createItem(data, picture, user_id)
        result['item'] = item
        
        categorySlug = CategoryModel.getCategorySlug(item.category_id)
        result['slug'] = categorySlug

        return result
