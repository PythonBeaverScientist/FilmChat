# -*- coding: Windows-1251 -*-
# ������� FastAPI
from fastapi import FastAPI

# �������, ��������� � ��
from create_db_engine import db_engine
from db_modul.film_orms import Base

# ������� ��������
from app.views.welcome_page import create_welcome
from films_views import router as film_router
from users.views import router as user_router


# �������� ���������� � ��������� � ���� ��������
app = FastAPI()

app.include_router(film_router)
app.include_router(user_router)


def create_db():
    Base.metadata.create_all(db_engine)


def drop_db():
    Base.metadata.drop_all(db_engine)


@app.get("/")
def index():
    return create_welcome()


# if __name__ == '__main__':
#     drop_db()
#     create_db()
#     film_scheme = handle_film_request()
