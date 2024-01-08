# -*- coding: Windows-1251 -*-

from pydantic import BaseModel, Field
from typing import List, Optional


class FilmModel(BaseModel):
    kinopoiskId: int
    nameRu: Optional[str] = Field(default=None)
    nameOriginal: Optional[str] = Field(default=None)
    posterUrl: Optional[str] = Field(default=None)
    ratingKinopoisk: Optional[float] = Field(default=None)
    ratingImdb: Optional[float] = Field(default=None)
    ratingFilmCritics: Optional[float] = Field(default=None)
    webUrl: Optional[str] = Field(default=None)
    year: Optional[int] = Field(default=None)
    filmLength: Optional[int] = Field(default=None)
    description: Optional[str] = Field(default=None)
    countries: Optional[List[dict]] = Field(default=None)
    genres: Optional[List[dict]] = Field(default=None)
    serial: Optional[bool] = Field(default=None)


class ShortFilmModel(BaseModel):
    filmId: int
    nameRu: Optional[str] = Field(default=None)
    nameEn: Optional[str] = Field(default=None)
    year: Optional[int] = Field(default=None)
    description: Optional[str] = Field(default=None)
    filmLength: Optional[str] = Field(default=None)
    countries: Optional[List[dict]] = Field(default=None)
    genres: Optional[List[dict]] = Field(default=None)
    posterUrl: Optional[str] = Field(default=None)
