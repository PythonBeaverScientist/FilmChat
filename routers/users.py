from fastapi import APIRouter

from schemas.users import UserModel
from controllers.users import create_user

router = APIRouter(prefix='/user', tags=['user'])


@router.post("/", response_model=UserModel, status_code=201)
def register(user_in: dict):
    user_saved = create_user(user_in)
    return user_saved
