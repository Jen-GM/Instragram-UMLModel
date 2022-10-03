import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    Firstname = Column(String(20), nullable=False)
    Lastname = Column(String(20), nullable=True)
    email = Column(String(20), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    origin_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    followed_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)

class Photo(Base):
    __tablename__ = 'photo'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    photo = Column(String(250), nullable=False)
    

class Location(Base):
    __tablename__ = 'location'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    location_text = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    userPost_ID = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    commentPost_ID = Column(Integer, ForeignKey('comment.id'))
    comment = relationship(Comment)

    photoPost_ID = Column(Integer, ForeignKey('photo.id'))
    photo = relationship(Photo)

    locationPost_ID = Column(Integer, ForeignKey('location.id'))
    location = relationship(Location)
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'instagram.png')