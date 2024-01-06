from fastapi import APIRouter

from users.schemas import UserModel
from users.crud import create_user

router = APIRouter(prefix='/user', tags=['user'])


@router.post("/", response_model=UserModel, status_code=201)
def register(user_in: dict):
    user_saved = create_user(user_in)
    return user_saved
