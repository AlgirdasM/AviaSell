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


class ItemModel():
    # get all objects from category, also get user information for
    def getAll(cid):
        q = session.query(CategoryItem, User.email)\
            .filter(CategoryItem.category_id == cid)\
            .filter(User.id == CategoryItem.user_id)\
            .all()

        return q
