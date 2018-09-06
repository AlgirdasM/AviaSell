# AviaSell app

This is a full stack app to sell aviation gear online.

## Setup instructions
1. Clone and setup [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
1. ssh to the virtual machine
2. cd /vagrant
3. Clone this repository to catalog folder
4. cd catalog
5. Populate fake database by running `python3 create_fake_db.py`
6. Run `python3 application.py`
7. Open browser and type http://localhost:8000/

## Database
Populate fake database - `python3 create_fake_db.py`
In production mode, populate only categories - `python3 create_categories.py`, content will be created by users.

## API endpoints

Category list with latest item
/api/v1/category
Category - id, name, picture, slug
Latest Item - id, title, description, location, picture, price

Category page with items(default page - 1)
/api/v1/category/<string:category_slug>/
/api/v1/category/<string:category_slug>/<int:page>'
Category - name
Items - id, title, description, location, picture, price
Total items and pages

Item data
/api/v1/item/<int:item_id>
Item - id, title, description, location, picture, price, category id and user id

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
Please note flaskdist only copies images, css and js files.
You need to manually update html files.


## Licenses and huge thank you
* [Yeoman](https://yeoman.io/)
* [Google Fonts](https://fonts.google.com/)
* [Web app generator generator](https://github.com/yeoman/generator-webapp)
* [Unsplash](https://unsplash.com/)
* [Main Banner Photo by Jake Buonemani on Unsplash](https://unsplash.com/photos/J7jaiTITluE)
* [Facebook & Google login buttons](https://codepen.io/davidelrizzo/pen/vEYvyv)
* [Python](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)