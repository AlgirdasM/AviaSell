# import database managers
#-------------------------#
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database_setup import Base, Category
#from app import webapp

# ?check_same_thread=False because there is an error, if you don't add it
engine = create_engine('sqlite:///aviasell.db?check_same_thread=False')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


class CategoryModel():
    def getAll():
        result = session.query(Category).all()
        return result

    def getCategory(categorySlug):
        result = session.query(Category).filter_by(slug=categorySlug).first()
        return result
