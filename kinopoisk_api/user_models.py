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

#
# if __name__ == '__main__':
#     json_value = {'filmId': 843650, 'nameRu': 'Мстители: Финал', 'nameEn': 'Avengers: Endgame', 'type': 'FILM',
#                   'year': '2019',
#                   'description': 'Оставшиеся в живых члены команды Мстителей и их союзники должны разработать новый план, который поможет противостоять разрушительным действиям могущественного титана Таноса. После наиболее масштабной и трагической битвы в истории они не могут допустить ошибку.',
#                   'filmLength': '03:01', 'countries': [{'country': 'США'}],
#                   'genres': [{'genre': 'боевик'}, {'genre': 'драма'}, {'genre': 'приключения'},
#                              {'genre': 'фантастика'}], 'rating': '7.9', 'ratingVoteCount': 776841,
#                   'posterUrl': 'https://kinopoiskapiunofficial.tech/images/posters/kp/843650.jpg',
#                   'posterUrlPreview': 'https://kinopoiskapiunofficial.tech/images/posters/kp_small/843650.jpg'}
#     json_val2 = {'kinopoiskId': 838664, 'kinopoiskHDId': None, 'imdbId': 'tt1779952', 'nameRu': 'Мстители, общий сбор!',
#                  'nameEn': None, 'nameOriginal': 'Avengers Assemble!',
#                  'posterUrl': 'https://kinopoiskapiunofficial.tech/images/posters/kp/838664.jpg',
#                  'posterUrlPreview': 'https://kinopoiskapiunofficial.tech/images/posters/kp_small/838664.jpg',
#                  'coverUrl': None, 'logoUrl': None, 'reviewsCount': 0, 'ratingGoodReview': None,
#                  'ratingGoodReviewVoteCount': 0, 'ratingKinopoisk': 6.8, 'ratingKinopoiskVoteCount': 258,
#                  'ratingImdb': 6.2, 'ratingImdbVoteCount': 255, 'ratingFilmCritics': None,
#                  'ratingFilmCriticsVoteCount': 0, 'ratingAwait': None, 'ratingAwaitCount': 0, 'ratingRfCritics': None,
#                  'ratingRfCriticsVoteCount': 0, 'webUrl': 'https://www.kinopoisk.ru/film/838664/', 'year': 2010,
#                  'filmLength': None, 'slogan': None, 'description': None, 'shortDescription': None,
#                  'editorAnnotation': None, 'isTicketsAvailable': False, 'productionStatus': None, 'type': 'TV_SERIES',
#                  'ratingMpaa': None, 'ratingAgeLimits': None, 'countries': [{'country': 'США'}],
#                  'genres': [{'genre': 'комедия'}], 'startYear': 2010, 'endYear': 2010, 'serial': True,
#                  'shortFilm': False, 'completed': True, 'hasImax': False, 'has3D': False,
#                  'lastSync': '2023-12-14T21:16:05.871554'}
#     json_val3 = {'kinopoiskId': 301, 'kinopoiskHDId': '4824a95e60a7db7e86f14137516ba590', 'imdbId': 'tt0133093',
#                  'nameRu': 'Матрица', 'nameEn': None, 'nameOriginal': 'The Matrix',
#                  'posterUrl': 'https://kinopoiskapiunofficial.tech/images/posters/kp/301.jpg',
#                  'posterUrlPreview': 'https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg',
#                  'coverUrl': 'https://avatars.mds.yandex.net/get-ott/2419418/2a0000017c27e0e090b55381c1b06e5c5b0b/orig',
#                  'logoUrl': None, 'reviewsCount': 315, 'ratingGoodReview': 89.0, 'ratingGoodReviewVoteCount': 260,
#                  'ratingKinopoisk': 8.5, 'ratingKinopoiskVoteCount': 712894, 'ratingImdb': 8.7,
#                  'ratingImdbVoteCount': 2015200, 'ratingFilmCritics': 7.7, 'ratingFilmCriticsVoteCount': 207,
#                  'ratingAwait': None, 'ratingAwaitCount': 0, 'ratingRfCritics': 60.0, 'ratingRfCriticsVoteCount': 5,
#                  'webUrl': 'https://www.kinopoisk.ru/film/301/', 'year': 1999, 'filmLength': 136,
#                  'slogan': 'Добро пожаловать в реальный мир',
#                  'description': 'Жизнь Томаса Андерсона разделена на\xa0две части: днём он\xa0—\xa0самый обычный офисный работник, получающий нагоняи от\xa0начальства, а\xa0ночью превращается в\xa0хакера по\xa0имени Нео, и\xa0нет места в\xa0сети, куда он\xa0бы не\xa0смог проникнуть. Но\xa0однажды всё меняется. Томас узнаёт ужасающую правду о\xa0реальности.',
#                  'shortDescription': 'Хакер Нео узнает, что его мир — виртуальный. Выдающийся экшен, доказавший, что зрелищное кино может быть умным',
#                  'editorAnnotation': None, 'isTicketsAvailable': False, 'productionStatus': None, 'type': 'FILM',
#                  'ratingMpaa': 'r', 'ratingAgeLimits': 'age16',
#                  'countries': [{'country': 'США'}, {'country': 'Австралия'}],
#                  'genres': [{'genre': 'фантастика'}, {'genre': 'боевик'}], 'startYear': None, 'endYear': None,
#                  'serial': False, 'shortFilm': False, 'completed': False, 'hasImax': False, 'has3D': False,
#                  'lastSync': '2023-12-30T03:05:58.857746'}
#     film_model = FilmModel(**json_val3)
#     print(film_model.model_dump())
#     print(film_model)
#     short_film_model = ShortFilmModel(**json_value)
#     print(short_film_model)
