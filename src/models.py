import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'Usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(10), nullable=False)
    fecha_subscripcion = Column(String(10), nullable=False)

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    Usuario_id = Column(Integer, ForeignKey('Usuarios.id'))
    Post_id = Column(Integer, ForeignKey('Post.id'))
    usuario = relationship(Usuarios)
    post = relationship(Post)

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    Usuario_id = Column(Integer, ForeignKey('Usuarios.id'))
    usuario = relationship(Usuarios)

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(Number, nullable=False)
    url = Column(String(250), nullable=False)
    Post_id = Column(Integer, ForeignKey('Post.id'))
    post = relationship(Post)

class Follower(Base):
    __tablename__ = 'Post'
    user_from_id = Column(Integer, ForeignKey('Usuarios.id'))
    user_to_id = Column(Integer, ForeignKey('Usuarios.id'))
    usuario_from = relationship(Usuarios)
    usuario_to = relationship(Usuarios)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e