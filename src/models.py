import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

# Clase para representar a los usuarios
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    publicaciones = relationship('Post', back_populates='usuario')  # Relación uno a muchos (un usuario puede tener muchas publicaciones)
    comentarios = relationship('Comentario', back_populates='usuario')  # Relación uno a muchos (un usuario puede hacer muchos comentarios)

# Clase para representar las publicaciones de los usuarios
class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    img_url = Column(String(250), nullable=False)
    likes_count = Column(Integer, nullable=False)
    usuario = relationship('Usuario', back_populates='publicaciones')  # Relación muchos a uno (muchos posts pueden pertenecer a un usuario)
    comentarios = relationship('Comentario', back_populates='post')  # Relación uno a muchos (un post puede tener muchos comentarios)

# Clase para representar los comentarios en las publicaciones
class Comentario(Base):
    __tablename__ = 'comentario'
    comentario_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.post_id'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    usuario = relationship('Usuario', back_populates='comentarios')  # Relación muchos a uno (muchos comentarios pueden ser realizados por un usuario)
    post = relationship('Post', back_populates='comentarios')  # Relación muchos a uno (muchos comentarios pueden pertenecer a un post)

# Clase para representar la relación de seguir a otros usuarios
class Seguidores(Base):
    __tablename__ = 'seguidores'
    seguidores_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    seguidor_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    usuario = relationship('Usuario', back_populates='seguidores', foreign_keys=[usuario_id])  # Relación muchos a uno (muchos seguidores pueden seguir a un usuario)
    seguido = relationship('Usuario', back_populates='seguidos', foreign_keys=[seguidor_id])  # Relación muchos a uno (muchos usuarios pueden ser seguidos por un seguidor)

    def to_dict(self):
        return {}

# Generar el diagrama ER y guardarlo como 'diagram.png'
render_er(Base, 'diagram.png')
