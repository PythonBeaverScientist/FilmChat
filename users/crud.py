from sqlalchemy.orm import Session
from db_modul.users_db_actions import create_db_user
from users.schemas import UserModel
from create_db_engine import db_engine


def create_user(user_sample: dict) -> UserModel:
    user_model: UserModel = UserModel(**user_sample)
    user_model.hash_user_psw()
    with Session(db_engine) as db_session:
        create_db_user(db_session, user_model)
    return user_model
