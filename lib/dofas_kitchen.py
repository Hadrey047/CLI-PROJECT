from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define the association table
all_user = Table(
    'all_user',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('menu_id', Integer, ForeignKey('menus.id'))
)

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(Integer)
    
    # Define the many-to-many relationship with Menus
    menus = relationship('Menus', secondary=all_user, back_populates='users')
    restaurants = relationship('Restaurant', backref='user')

class Menus(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True)
    breakfast = Column(String)
    lunch = Column(String)
    dinner = Column(String)
    ethnic = Column(String)
    
    # Define the many-to-many relationship with Users
    users = relationship('Users', secondary=all_user, back_populates='menus')
    restaurants = relationship('Restaurant', backref='menu')

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    soft_drink = Column(String)
    alcoholic_drink = Column(String)
    wine = Column(String)

    # Define foreign keys for the relationships
    user_id = Column(Integer, ForeignKey('users.id'))
    menu_id = Column(Integer, ForeignKey('menus.id'))

