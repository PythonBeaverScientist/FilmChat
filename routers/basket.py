from fastapi import APIRouter

from users.crud import set_new_mark
from users.schemas import Mark

router = APIRouter(prefix='/basket', tags=['basket'])


@router.post("/", response_model=Mark, status_code=201)
def create_token(mark_data: dict):
    new_mark: Mark = set_new_mark(mark_data)
    return new_mark
