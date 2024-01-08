from datetime import datetime
from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED

from db_modul.orms import User, Token, DBMark
from schemas.users import UserModel, Mark


def create_db_user(db_session: Session, user_model: UserModel):
    user = User(**user_model.model_dump(), reg_date=datetime.now())
    statement = select(User).filter_by(user_name=str(user.user_name))
    query_res = db_session.scalars(statement).all()
    if not query_res:
        db_session.add(user)
        db_session.commit()
    else:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="User with this username already exists"
        )
    return user


def get_user(db_session, auth_use):
    statement = select(User).filter_by(user_name=str(auth_use.user_name))
    db_user: User = db_session.scalar(statement)
    if not db_user:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    else:
        return db_user


def create_user_token(session: Session, db_user: User):
    token = Token(access_token=str(uuid4()), user_id=db_user.user_id)
    session.add(token)
    session.commit()
    return token


def get_user_id_by_token(db_session: Session, access_token: str):
    statement = select(Token).filter_by(access_token=access_token)
    db_token: Token = db_session.scalar(statement)
    if db_token:
        return db_token.user_id
    else:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="There is no token for this user. Authenticate to get one."
        )


def create_mark(db_session: Session, mark_model: Mark):
    user_id = get_user_id_by_token(db_session, mark_model.access_token)
    db_mark: DBMark = DBMark(mark=mark_model.mark, user_id=user_id, film_id=mark_model.film_id)
    db_session.add(db_mark)
    db_session.commit()
    return db_mark
