#!/usr/bin/env python3

# import database managers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database_setup import Base, Category
from app import webapp

engine = create_engine(webapp.config['DATABASE_ENGINE'])
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


class CategoryModel():
    def getAll():
        # Get all categories
        result = session.query(Category).all()
        return result

    def getCategoryBySlug(categorySlug):
        # Get category by slug
        result = session.query(Category).filter_by(slug=categorySlug).one()
        return result

    def getCategorySlug(category_id):
        # Get category by id
        result = session.query(Category).filter_by(id=category_id).one()
        return result.slug
