from sqlalchemy.orm import Session
from db_modul.users_db_actions import create_db_user, get_user, create_user_token, create_mark
from users.schemas import UserModel, UserAuth, Mark
from create_db_engine import db_engine
from secure import psw_context
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST


def create_user(user_sample: dict) -> UserModel:
    user_model: UserModel = UserModel(**user_sample)
    user_model.hash_user_psw()
    with Session(db_engine) as db_session:
        create_db_user(db_session, user_model)
    return user_model


def authenticate(auth_data: dict):
    auth_use: UserAuth = UserAuth(**auth_data)
    with Session(db_engine) as session:
        db_user = get_user(session, auth_use)
        if not psw_context.verify(auth_use.password, db_user.password):
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Incorrect user password or username"
            )
        token = create_user_token(session, db_user)
        access_token = token.access_token
    return {"access_token": access_token}


def set_new_mark(mark_data: dict) -> Mark:
    mark_scheme: Mark = Mark(**mark_data)
    with Session(db_engine) as db_session:
        create_mark(db_session, mark_scheme)
    return mark_scheme
