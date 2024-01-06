# -*- coding: Windows-1251 -*-

from db_modul.film_db_actions import create_film, create_short_film
from kinopoisk_api.api_query import APIClient, RequestJson
from kinopoisk_api.user_models import FilmModel, ShortFilmModel
from create_db_engine import db_engine
import httpx
from sqlalchemy.orm import Session
from pydantic import ValidationError
from base_log import LoggerHand

log = LoggerHand(__name__, f"logs/{__name__}.log")


def handle_film_request(film_id: int):
    api_client = APIClient()
    with httpx.Client() as http_session:
        response = api_client.get_film_by_id(http_session, film_id)
        if 200 <= response.status_code < 300:
            req_json = RequestJson(response)
            json_res = req_json.serialize_response()
            try:
                film_scheme = FilmModel(**json_res)
                with Session(db_engine) as db_session:
                    create_film(db_session, film_scheme)
                    return film_scheme
            except ValidationError as err:
                log.logger.info(err)
                return None
        else:
            return None


def handle_search_request(key_word: str):
    api_client = APIClient()
    with httpx.Client() as http_session:
        response = api_client.get_films_lst_by_word(http_session, key_word)
        if 200 <= response.status_code < 300:
            req_json = RequestJson(response)
            json_res: dict = req_json.serialize_response()
            json_res: list = json_res.get('films')
            models_lst: list = []
            for sort_json_des in json_res:
                try:
                    short_film_scheme = ShortFilmModel(**sort_json_des)
                    models_lst.append(short_film_scheme)
                    with Session(db_engine) as db_session:
                        create_short_film(db_session, short_film_scheme)
                except ValidationError as err:
                    log.logger.info(err)
            return models_lst
        else:
            return None
