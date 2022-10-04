import os
import sys
import json
from sqlalchemy import Column, ForeignKey, Integer, String, TypeDecorator, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy_media import StoreManager, FileSystemStore, Image, ImageAnalyzer, ImageValidator, ImageProcessor
from eralchemy import render_er


Base = declarative_base()

class Json(TypeDecorator):
    impl = Unicode

    def process_bind_param(self, value, engine):
        return json.dumps(value)

    def process_result_value(self, value, engine):
        if value is None:
            return None

        return json.loads(value)

class UserPicture(Image):
    __pre_processors__ = [
        ImageAnalyzer(),
        ImageValidator(
            minimum=(80, 80),
            maximum=(800, 600),
            min_aspect_ratio=1.2,
            content_types=['image/jpeg', 'image/png']
        ),
        ImageProcessor(
            fmt='jpeg',
            width=120,
            crop=dict(
                left='10%',
                top='10%',
                width='80%',
                height='80%',
            )
        )
    ] 
    
class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    photo = Column(UserPicture.as_mutable(Json), nullable=False)
    URL = Column(String(70), nullable=True)

class User(Base):   
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    Firstname = Column(String(20), nullable=False)
    Lastname = Column(String(20), nullable=True)
    email = Column(String(20), nullable=False)

    post = relationship("Post", backref="User")

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    userCommenter_ID = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)


    commentPost_ID = Column(Integer, ForeignKey('comment.id'))
    comment = relationship(Comment)

    mediaPost_ID = Column(Integer, ForeignKey('media.id'))
    media = relationship(Media)

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    origin_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    followed_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'instagram.png')