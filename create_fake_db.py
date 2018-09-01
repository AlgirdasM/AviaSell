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


#----------------------------Users---------------------------
user1 = User(name='Sebastian Thrun',
             email='sebastianthrun@udacity.local',
             picture='https://avatars3.githubusercontent.com/u/16962421?s=400&v=4'
             )
session.add(user1)
session.commit()
#--------------------------End Users-------------------------


#----------------------------Items---------------------------
item1 = CategoryItem(title='Airplane 1',
             description='4. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='Portland, OR, USA',
             picture='andrew-palmer-255954-unsplash.jpg',
             price='$203400',
             category_id='1',
             user_id='1',
             )
session.add(item1)
session.commit()

item2 = CategoryItem(title='Airplane 2',
             description='Consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='Las Vegas, LA, USA',
             picture='john-mcarthur-603901-unsplash.jpg',
             price='$20500',
             category_id='1',
             user_id='1',
             )
session.add(item2)
session.commit()

item3 = CategoryItem(title='Airplane 3',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='Paris, France',
             picture='leon-liu-483622-unsplash.jpg',
             price='$41100',
             category_id='1',
             user_id='1',
             )
session.add(item3)
session.commit()

item4 = CategoryItem(title='Airplane 4',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='Berlin, Germany',
             picture='randy-fath-722451-unsplash.jpg',
             price='$41200',
             category_id='1',
             user_id='1',
             )
session.add(item4)
session.commit()


item5 = CategoryItem(title='Helicopter 1',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='Berlin, Germany',
             picture='don-jackson-wyatt-566286-unsplash.jpg',
             price='$41200',
             category_id='2',
             user_id='1',
             )
session.add(item5)
session.commit()

item6 = CategoryItem(title='Helicopter 2',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='ibrahim-rifath-745387-unsplash.jpg',
             price='$41200',
             category_id='2',
             user_id='1',
             )
session.add(item6)
session.commit()

item7 = CategoryItem(title='Helicopter 3',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='ivo-paul-van-vliet-479547-unsplash.jpg',
             price='$41200',
             category_id='2',
             user_id='1',
             )
session.add(item7)
session.commit()

item8 = CategoryItem(title='Helicopter 4',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='melanie-dretvic-698186-unsplash.jpg',
             price='$41200',
             category_id='2',
             user_id='1',
             )
session.add(item8)
session.commit()


item9 = CategoryItem(title='Glider 1',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='fal-enron-637983-unsplash.jpg',
             price='$41200',
             category_id='3',
             user_id='1',
             )
session.add(item9)
session.commit()


item10 = CategoryItem(title='Hot Air Balloon 1',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='andrea-krug-794226-unsplash.jpg',
             price='$41200',
             category_id='4',
             user_id='1',
             )
session.add(item10)
session.commit()

item11 = CategoryItem(title='Hot Air Balloon 2',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='austin-ban-401-unsplash.jpg',
             price='$41200',
             category_id='4',
             user_id='1',
             )
session.add(item11)
session.commit()

item12 = CategoryItem(title='Hot Air Balloon 3',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='ravali-yan-96009-unsplash.jpg',
             price='$41200',
             category_id='4',
             user_id='1',
             )
session.add(item12)
session.commit()

item13 = CategoryItem(title='Hot Air Balloon 4',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='sebastien-gabriel-127043-unsplash.jpg',
             price='$41200',
             category_id='4',
             user_id='1',
             )
session.add(item13)
session.commit()

item14 = CategoryItem(title='Hot Air Balloon 5',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='songeunyoung-467-unsplash.jpg',
             price='$41200',
             category_id='4',
             user_id='1',
             )
session.add(item14)
session.commit()


item15 = CategoryItem(title='Paraglider 1',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='anton-repponen-99617-unsplash.jpg',
             price='$41200',
             category_id='5',
             user_id='1',
             )
session.add(item15)
session.commit()

item16 = CategoryItem(title='Paraglider 2',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='bill-mackie-622760-unsplash.jpg',
             price='$41200',
             category_id='5',
             user_id='1',
             )
session.add(item16)
session.commit()

item17 = CategoryItem(title='Paraglider 3',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='emanuele-vercesi-564161-unsplash.jpg',
             price='$41200',
             category_id='5',
             user_id='1',
             )
session.add(item17)
session.commit()

item18 = CategoryItem(title='Paraglider 4',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='jairph-399672-unsplash.jpg',
             price='$41200',
             category_id='5',
             user_id='1',
             )
session.add(item18)
session.commit()

item19 = CategoryItem(title='Paraglider 5',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='kiki-siepel-583489-unsplash.jpg',
             price='$41200',
             category_id='5',
             user_id='1',
             )
session.add(item19)
session.commit()

item20 = CategoryItem(title='Other 1',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='dan-lohmar-617043-unsplash.jpg',
             price='$41200',
             category_id='5',
             user_id='1',
             )
session.add(item20)
session.commit()

item21 = CategoryItem(title='Other 1',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='inspirationfeed-97073-unsplash.jpg',
             price='$41200',
             category_id='6',
             user_id='1',
             )
session.add(item21)
session.commit()

item22 = CategoryItem(title='Other 2',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='jp-valery-747651-unsplash.jpg',
             price='$41200',
             category_id='6',
             user_id='1',
             )
session.add(item22)
session.commit()

item23 = CategoryItem(title='Other 3',
             description='Sit amet, consectetur adipiscing elit. Etiam dignissim scelerisque arcu. Donec hendrerit nisi posuere, aliquam nunc quis, consequat dui. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a posuere metus, at rhoncus dolor. Praesent ullamcorper sit amet risus et tincidunt. Donec et venenatis enim. Cras dictum, sem ut faucibus commodo, nibh ex imperdiet est, sed semper nunc.',
             location='London, United Kingdom',
             picture='matthieu-joannon-687144-unsplash.jpg',
             price='$41200',
             category_id='6',
             user_id='1',
             )
session.add(item23)
session.commit()
#--------------------------End Items-------------------------