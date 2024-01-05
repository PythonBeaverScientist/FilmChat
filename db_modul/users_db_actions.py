from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from db_modul.user_orms import User
from users.schemas import UserModel


def create_db_user(db_session: Session, user_model: UserModel):
    user = User(**user_model.model_dump(), reg_date=datetime.now())
    statement = select(User).filter_by(user_name=str(user.user_name))
    query_res = db_session.scalars(statement).all()
    if not query_res:
        db_session.add(user)
        db_session.commit()
    return user
