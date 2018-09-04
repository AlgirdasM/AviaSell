#!/usr/bin/env python3

from app.models import *


class CategoryController():
    def categoriesWithLatestItem():
        # Get all categories
        categories = CategoryModel.getAll()
        # Create result array
        result = []
        # Append category and item to result
        for category in categories:
            result.append((category, ItemModel.getLatestItem(category.id)))
        return result

    def getAllCategories():
        result = CategoryModel.getAll()
        return result

    def validateSlug(slug):
        try:
            result = CategoryModel.getCategoryBySlug(slug)
            return True
        except:
            return False