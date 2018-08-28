#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask import redirect, url_for, flash, jsonify
app = Flask(__name__)

# import database managers
#-------------------------#
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, CategoryItem

# ?check_same_thread=False because there is an error, if you don't add it
engine = create_engine('sqlite:///aviasell.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#------------------------Index-------------------------
@app.route('/')
def main():
    return "This is main page"
#----------------------Index End-----------------------


#------------------------Login-------------------------
@app.route('/login')
def login():
    return "This is login page"
#-----------------------Login End----------------------


#-----------------------Category-----------------------
# Read category
@app.route('/category/<string:category_name>/')
def category(category_name):
    return "This is " + category_name + " category"
#---------------------Category End---------------------


#------------------------Items-------------------------
# Create new item
@app.route('/category/<string:category_name>/create', methods=['GET', 'POST'])
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
@app.route('/category/<string:category_name>/<int:item_id>/<string:item_name>/')
def item(category_name, item_name, item_id):
    return "Item " + item_name + " with id: " + str(item_id) + " in category " + category_name


# Update item
@app.route('/category/<string:category_name>/<int:item_id>/update', methods=['GET', 'POST'])
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
@app.route('/category/<string:category_name>/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(category_name, item_id):
    if request.method == 'POST':
        return "Deleting item id: " + str(item_id)
    else:
        return "Edit: item with id: " + str(item_id) + " in category " + category_name
#----------------------End Items-----------------------


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
