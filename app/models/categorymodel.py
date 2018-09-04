#!/usr/bin/env python3

# import database managers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database_setup import Base, Category

# ?check_same_thread=False because there is an error, if you don't add it
engine = create_engine('sqlite:///aviasell.db?check_same_thread=False')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


class CategoryModel():
    def getAll():
        result = session.query(Category).all()
        return result

    def getCategoryBySlug(categorySlug):
        result = session.query(Category).filter_by(slug=categorySlug).one()
        return result

    def getCategorySlug(category_id):
        result = session.query(Category).filter_by(id=category_id).one()
        return result.slug
