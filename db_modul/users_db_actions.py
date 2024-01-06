from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from db_modul.film_orms import User
from users.schemas import UserModel


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
