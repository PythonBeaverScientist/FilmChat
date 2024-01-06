# -*- coding: Windows-1251 -*-

from sqlalchemy import ForeignKey, String, Column, Integer, DateTime, Boolean, Text, JSON, Float
from sqlalchemy.orm import relationship, declarative_base
import json
from base_log import LoggerHand

log = LoggerHand(__name__, f"logs/{__name__}.log")
Base = declarative_base()


def base_repr(sample):
    dct: dict = dict()
    dct['tablename'] = str(sample.__tablename__)
    for elem in sample.__dict__.items():
        if isinstance(elem[1], str) or isinstance(elem[1], float) or isinstance(elem[1], dict) \
                or isinstance(elem[1], int) or isinstance(elem[1], list) or isinstance(elem[1], bool):
            dct[elem[0]] = elem[1]
    return json.dumps(dct, ensure_ascii=False)


class Film(Base):
    __tablename__ = 'films'
    kinopoiskId: Column = Column(Integer, primary_key=True)
    nameRu: Column = Column(String(200), nullable=True)
    nameOriginal: Column = Column(String(200), nullable=True)
    posterUrl: Column = Column(String(200), nullable=True)
    ratingKinopoisk: Column = Column(Float, nullable=True)
    ratingImdb: Column = Column(Float, nullable=True)
    ratingFilmCritics: Column = Column(Float, nullable=True)
    webUrl: Column = Column(String(200), nullable=True)
    year: Column = Column(Integer, nullable=True)
    filmLength: Column = Column(Float, nullable=True)
    description: Column = Column(Text, nullable=True)
    countries: Column = Column(JSON, nullable=True)
    genres: Column = Column(JSON, nullable=True)
    serial: Column = Column(Boolean, nullable=True)

    def __str__(self):
        return base_repr(self)


class ShortFilm(Base):
    __tablename__ = 'short_films'
    filmId: Column = Column(Integer, primary_key=True)
    nameRu: Column = Column(String(200), nullable=True)
    nameEn: Column = Column(String(200), nullable=True)
    year: Column = Column(Integer, nullable=True)
    description: Column = Column(Text, nullable=True)
    filmLength: Column = Column(String(200), nullable=True)
    countries: Column = Column(JSON, nullable=True)
    genres: Column = Column(JSON, nullable=True)
    posterUrl: Column = Column(String(200), nullable=True)

    def __str__(self):
        return base_repr(self)

class User(Base):
    __tablename__ = 'users'
    user_id: Column = Column(Integer, primary_key=True)
    user_name: Column = Column(String(200), unique=True)
    password: Column = Column(String(200))
    email: Column = Column(String(200))
    first_name: Column = Column(String(200))
    last_name: Column = Column(String(200))
    birth_date: Column = Column(DateTime, nullable=True)
    reg_date: Column = Column(DateTime)

    tokens = relationship('Token', back_populates='user')
    
    
class Token(Base): 
    __tablename__ = 'tokens'
    token_id: Column = Column(Integer, primary_key=True)
    access_token: Column = Column(String(200), unique=True, index=True)
    user_id: Column = Column(Integer, ForeignKey("users.user_id"))

    user = relationship('User', back_populates='tokens')

    def __str__(self):
        return base_repr(self)
