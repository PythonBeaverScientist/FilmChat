# -*- coding: Windows-1251 -*-

import httpx
import json
from typing import List, Optional


class APIClient:
    def __init__(self):
        token_path: str = 'credentials/kinopoisk_credentials.json'
        with open(token_path, 'r') as api_file:
            credentials: dict = json.load(api_file)
        self.BASE_URL: str = credentials.get('base_url')
        self.TOKEN: str = credentials.get('token')
        self.headers: dict = {
            'X-API-KEY': self.TOKEN,
            'Content-Type': 'application/json'
        }
        self.old_method: str = 'v2.1'
        self.new_method: str = 'v2.2'

    def get_film_by_id(self, http_session: httpx.Client, film_id: int) -> Optional[httpx.Response]:
        film_url: str = f"{self.BASE_URL}/{self.new_method}/films/{film_id}"
        film_res: httpx.Response = http_session.get(url=film_url, headers=self.headers)
        if 200 <= film_res.status_code < 400:
            return film_res
        else:
            return None

    def get_films_lst_by_word(self, http_session: httpx.Client, search_keyword: str) -> Optional[httpx.Response]:
        lst_url: str = f"{self.BASE_URL}/{self.old_method}/films/search-by-keyword?keyword={search_keyword}"
        lst_res: httpx.Response = http_session.get(url=lst_url, headers=self.headers)
        if 200 <= lst_res.status_code < 400:
            return lst_res
        else:
            return None


class RequestJson:
    def __init__(self, response: httpx.Response):
        self.response: httpx.Response = response

    def serialize_response(self):
        return self.response.json()