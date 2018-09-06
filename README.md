# AviaSell app
AviaSell is a full stack app to sell aviation gear online. Written in Python3 using MVC design pattern. Use Facebook or Google to log in to the app - it also creates a user in the database if a user doesn't exist in our system. After the login user can make CRUD operations on items. It performs local permission check and also verifies if the user is logged in before trying to edit or delete an item.


## Setup instructions
1. Clone and setup [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
1. ssh to the virtual machine
2. cd /vagrant
3. Clone this repository to catalog folder
4. cd catalog
5. Populate fake database by running `python3 create_fake_db.py`
6. Run `python3 application.py`
7. Open browser and type http://localhost:8000/

## Config
Config file is located at app/config/webapp.cfg
Also in the same folder there are both JSON files for Google and Facebook oauth login

## API endpoints
**/api/v1
**/api/v1/category**
*Category list with latest item. Returns*
* Category: id, name, picture, slug
* Latest Item: id, title, description, location, picture, price


**/api/v1/category/<string:category_slug>/**
**/api/v1/category/<string:category_slug>/<int:page>**
*Category page with items(default page - 1). Returns*
* Category: name
* Items: id, title, description, location, picture, price
* Total items
* Total pages


**/api/v1/item/<int:item_id>**
*Item data. Returns*
* Item: id, title, description, location, picture, price, category id and user id

## Frontend(optional, may be used for development)
Frontend created using [Yeoman](http://yeoman.io/) [Web app generator generator](https://github.com/yeoman/generator-webapp).

To install dependencies run:
1. `cd frontend`
2. `npm install`
3. `bower install`

To serve development server:
* Run `gulp serve`

To generate production version for Flask:
* Run `gulp build`
* Run `gulp flaskdist`

*Please note flaskdist only copies images, css and js files.
You need to manually update html files.*

## Licenses and huge thank you
* [Facebook login](https://developers.facebook.com/)
* [Facebook & Google login buttons](https://codepen.io/davidelrizzo/pen/vEYvyv)
* [Flask](http://flask.pocoo.org/)
* [Google Fonts](https://fonts.google.com/)
* [Google Login](https://console.developers.google.com/)
* [Main Banner Photo by Jake Buonemani on Unsplash](https://unsplash.com/photos/J7jaiTITluE)
* [Python](https://www.python.org/)
* [Udacity](https://eu.udacity.com/)
* [Unsplash](https://unsplash.com/)
* [Web app generator generator](https://github.com/yeoman/generator-webapp)
* [Yeoman](https://yeoman.io/)