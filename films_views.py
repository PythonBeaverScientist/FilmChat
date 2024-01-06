from kinopoisk_api.controller import handle_film_request, handle_search_request
from fastapi import APIRouter

router = APIRouter(prefix='/films', tags=['films'])


@router.get("")
def film_by_index(film_id: int):
    return handle_film_request(film_id)


@router.get("/search")
def film_by_keyword(key_word: str):
    return handle_search_request(key_word)