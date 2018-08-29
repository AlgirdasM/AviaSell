#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database_setup import Base, User, Category, CategoryItem

# ?check_same_thread=False because there is an error, if you don't add it
engine = create_engine('sqlite:///aviasell.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


item1 = CategoryItem(title="Lorem ipsum dolor",
             description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.",
             location="Portland, OR, USA",
             picture="https://loremflickr.com/500/333/aircraft",
             price="$2000",
             category_id="1",
             user_id="1",
             )
session.add(item1)
session.commit()

item2 = CategoryItem(title="Lorem ipsum dolor",
             description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.",
             location="Portland, OR, USA",
             picture="https://loremflickr.com/500/333/aircraft",
             price="$2000",
             category_id="1",
             user_id="1",
             )
session.add(item2)
session.commit()

item3 = CategoryItem(title="Lorem ipsum dolor",
             description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.",
             location="Portland, OR, USA",
             picture="https://loremflickr.com/500/333/aircraft",
             price="$2000",
             category_id="1",
             user_id="2",
             )
session.add(item3)
session.commit()