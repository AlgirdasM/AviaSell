#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database_setup import Base, User, Category, CategoryItem

# ?check_same_thread=False because there is an error, if you don't add it
engine = create_engine('sqlite:///aviasell.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


user1 = User(name='Linus Torvalds',
             email='tinustorvalds@linux.local',
             picture='https://avatars1.githubusercontent.com/u/1024025?s=400&v=4'
             )
session.add(user1)
session.commit()


user2 = User(name='Sebastian Thrun',
             email='sebastianthrun@udacity.local',
             picture='https://avatars3.githubusercontent.com/u/16962421?s=400&v=4'
             )
session.add(user2)
session.commit()