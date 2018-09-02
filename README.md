# AviaSell app

This is a full stack app to sell aviation gear online.

## Database
Populate fake database - `python3 create_fake_db.py`
Production mode, populate categories - `python3 create_categories.py`

## Frontend
Frontend created using [Yeoman](http://yeoman.io/) [Web app generator generator](https://github.com/yeoman/generator-webapp).

To install dependencies run:
1. `cd frontend`
2. `npm install`
3. `bower install`

To serve development server:
* Run `gulp serve`

To generate production version for Flask:
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