from fastapi import APIRouter

from controllers.users import authenticate
from schemas.users import Token

router = APIRouter(prefix='/tokens', tags=['token'])


@router.post("/", response_model=Token, status_code=201)
def create_token(auth_data: dict):
    new_token: dict = authenticate(auth_data)
    return new_token
