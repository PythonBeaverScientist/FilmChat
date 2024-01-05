from fastapi import APIRouter

from users.schemas import UserModel
from users.crud import create_user

router = APIRouter(prefix='/user', tags=['user'])


@router.post("/", response_model=UserModel)
def create_new_user(user_in: dict):
    user_saved = create_user(user_in)
    return user_saved
