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
        result = session.query(CategoryItem, User.email)\
            .filter(CategoryItem.category_id == cid)\
            .filter(User.id == CategoryItem.user_id)\
            .all()
        return result


    def getItem(item_id):
        result = session.query(CategoryItem).filter_by(id=item_id).one()
        return result

    def getLatestItem(category_id):
        result = session.query(CategoryItem).filter_by(category_id=category_id).order_by(CategoryItem.created_date.desc()).first()
        return result

    def createItem(item, category_id, user_id):
        addItem = CategoryItem(title = item['title'],
            description = item['description'],
            location = item['location'],
            picture = item['picture'],
            price = item['price'],
            category_id = category_id,
            user_id = user_id)
        session.add(addItem)
        session.commit()

        return 'created'