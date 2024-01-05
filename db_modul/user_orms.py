from sqlalchemy import ForeignKey, String, Column, Integer, DateTime, Boolean, Text, JSON, Float, select
from sqlalchemy.orm import relationship, declarative_base
from base_log import LoggerHand
from db_modul.film_orms import base_repr, Base

log = LoggerHand(__name__, f"logs/{__name__}.log")


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
