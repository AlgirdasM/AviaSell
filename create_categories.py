#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database_setup import Base, User, Category, CategoryItem

# ?check_same_thread=False because there is an error, if you don't add it
engine = create_engine('sqlite:///aviasell.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


#-------------------------Categories-------------------------
category1 = Category(name='Airplane',
                     picture='rodrigo-rodriguez-102662-unsplash.jpg',
                     description='Airplane by Rodrigo Rodriguez on Unsplash',
                     slug='airplane')
session.add(category1)
session.commit()

category2 = Category(name='Helicopter',
                     picture='neil-thomas-738058-unsplash.jpg',
                     description='Helicopter by Neil Thomas on Unsplash',
                     slug='helicopter')
session.add(category2)
session.commit()

category3 = Category(name='Glider',
                     picture='konrad-wojciechowski-110181-unsplash.jpg',
                     description='Glider by Konrad Wojciechowski on Unsplash',
                     slug='glider')
session.add(category3)
session.commit()

category4 = Category(name='Lighter than air',
                     picture='ellehem-693-unsplash.jpg',
                     description='Air Balloon by Ellehem on Unsplash',
                     slug='lighter-than-air')
session.add(category4)
session.commit()

category5 = Category(name='Paraglider',
                     picture='pablo-heimplatz-275434-unsplash.jpg',
                     description='Paraglider by Pablo Heimplatz on Unsplash',
                     slug='paraglider')
session.add(category5)
session.commit()

category6 = Category(name='Other',
                     picture='oxana-v-524239-unsplash.jpg',
                     description='Picture by Oxana V on Unsplash',
                     slug='other')
session.add(category6)
session.commit()
#-----------------------End Categories-----------------------
