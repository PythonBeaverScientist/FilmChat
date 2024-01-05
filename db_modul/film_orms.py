# -*- coding: Windows-1251 -*-
import datetime

from sqlalchemy import ForeignKey, String, Column, Integer, DateTime, Boolean, Text, JSON, Float, select
from sqlalchemy.orm import relationship, declarative_base
from kinopoisk_api.user_models import FilmModel, ShortFilmModel
from db_modul.db_client import DBClient
import json
import hashlib
from base_log import LoggerHand
from psycopg2 import errors

UniqueViolation = errors.lookup('23505')
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

    def __str__(self):
        return base_repr(self)


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


def create_user(db_session):
    hash_obj = hashlib.new('md5')
    hash_obj.update(b'12345')
    password = hash_obj.hexdigest()
    user = User(user_name='Dmitriy',  password=password, email='tokamak663@gmail.com',
                first_name='Дмитрий', last_name='Щукин', reg_date=datetime.datetime.now())
    statement = select(User).filter_by(user_name=str(user.user_name))
    query_res = db_session.scalars(statement).all()
    if not query_res:
        db_session.add(user)
        db_session.commit()
    return user


def create_film(db_session, film_scheme: FilmModel):
    db_film_model: Film = Film(**film_scheme.model_dump())
    query_res = db_session.get(Film, int(film_scheme.kinopoiskId))
    if query_res is None:
        db_session.add(db_film_model)
        db_session.commit()
    return db_film_model


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


def create_short_film(db_session, film_scheme: ShortFilmModel):
    db_short_film_model: ShortFilm = ShortFilm(**film_scheme.model_dump())
    query_res = db_session.get(ShortFilm, int(film_scheme.filmId))
    if query_res is None:
        db_session.add(db_short_film_model)
        db_session.commit()
    return db_short_film_model


# if __name__ == '__main__':
#     db_client: DBClient = DBClient()
#     db_engine = db_client.create_sql_alchemy_engine()
#     ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#     print(ROOT_DIR)
#     Base.metadata.drop_all(db_engine)
#     Base.metadata.create_all(db_engine)
