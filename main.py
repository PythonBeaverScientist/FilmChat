# -*- coding: Windows-1251 -*-

from db_modul.db_client import DBClient
from db_modul.film_orms import Base
from kinopoisk_api.controller import handle_film_request, handle_search_request
from fastapi import FastAPI
from app.views.welcome_page import create_welcome

app = FastAPI()
film_id: int = 302
key_word: str = "avengers"


def create_db():
    db_client: DBClient = DBClient()
    db_engine = db_client.create_sql_alchemy_engine()
    Base.metadata.create_all(db_engine)


def drop_db():
    db_client: DBClient = DBClient()
    db_engine = db_client.create_sql_alchemy_engine()
    Base.metadata.drop_all(db_engine)


@app.get("/")
def index():
    return create_welcome()



# if __name__ == '__main__':
#     drop_db()
#     create_db()
#     film_scheme = handle_film_request()
