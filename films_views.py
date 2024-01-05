from kinopoisk_api.controller import handle_film_request, handle_search_request
from fastapi import APIRouter

router = APIRouter(prefix='/films', tags=['films'])

film_id = 302
key_word = 'avengers'


@router.get(f"/{film_id}")
def film_by_index():
    return handle_film_request()


@router.get(f"/{key_word}")
def film_by_keyword():
    return handle_search_request()