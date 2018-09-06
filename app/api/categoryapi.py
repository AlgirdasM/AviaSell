#!/usr/bin/env python3

from app import webapp
from flask import jsonify
from app.controllers import *

@webapp.route('/api/v1')
@webapp.route('/api/v1/category')
def apiCategoriesWithLatestItem():
    # Get all categories with latest item
    data = CategoryController.categoriesWithLatestItem()
    # Create empty array to combine data
    categories = []
    for category, item in data:
        json = {}
        json['id'] = category.id
        json['name'] = category.name
        json['picture'] = category.picture
        json['slug'] = category.slug
        json['latest_item'] = {}
        json['latest_item']['id'] = item.id
        json['latest_item']['title'] = item.title
        json['latest_item']['description'] = item.description
        json['latest_item']['location'] = item.location
        json['latest_item']['picture'] = item.picture
        json['latest_item']['price'] = item.price
        categories.append(json)

    return jsonify(categories_with_latest_item=categories)


@webapp.route('/api/v1/category/<string:category_slug>/', defaults={'page': 1})
@webapp.route('/api/v1/category/<string:category_slug>/<int:page>')
def apiGetCategoryPage(category_slug, page):
    data = ItemController.getPageItems(category_slug, page)

    if data['code'] != 200:
        message = data['message']
        code = data['code']
        return jsonify(error=message, code=code), code

    # If page is greater than page count, return error
    if page > data['pageCount']:
        message = 'Page not found'
        code = 404
        return jsonify(error=message, code=code), code

        # Create empty array to combine data
    items = []
    for item, email in data['items']:
        json = {}
        json['item_id'] = item.id
        json['item_title'] = item.title
        json['item_description'] = item.description
        json['item_location'] = item.location
        json['item_picture'] = item.picture
        json['item_price'] = item.price
        items.append(json)

    # We got data, display it
    return jsonify(total_items=data['totalItems'],
                   pages=data['pageCount'],
                   items=items,
                   category_name=data['category_name'])


@webapp.route('/api/v1/item/<int:item_id>')
def apiGetItem(item_id):
    # Get item
    item = ItemController.getItemByID(item_id)
    return jsonify(item=item.serialize)
