#!/usr/bin/env python3

# import database managers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database_setup import Base, User, Category, CategoryItem

# ?check_same_thread=False because there is an error, if you don't add it
engine = create_engine('sqlite:///aviasell.db?check_same_thread=False')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


class UserModel():
    def getUser(uid):
        result = session.query(User).filter_by(id=uid).one()
        return result

    def getUserEmail(uid):
        result = session.query(User).filter_by(id=uid).one()
        return result.email

    def getUserID(email):
        try:
            user = session.query(User).filter_by(email=email).one()
            return user.id
        except:
            return None

    def createUser(login_session):
        newUser = User(name=login_session['username'], email=login_session[
                       'email'], picture=login_session['picture'])
        session.add(newUser)
        session.commit()
        user = session.query(User).filter_by(
            email=login_session['email']).one()
        return user.id
