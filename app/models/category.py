# import database managers
#-------------------------#
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database_setup import Base, User, Category, CategoryItem
#from app import webapp

# ?check_same_thread=False because there is an error, if you don't add it
engine = create_engine('sqlite:///aviasell.db?check_same_thread=False')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


class CategoryModel():
    def getAll():
        return session.query(Category).all()
