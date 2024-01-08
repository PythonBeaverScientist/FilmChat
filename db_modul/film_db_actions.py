from db_modul.orms import Film, ShortFilm
from schemas.films import FilmModel, ShortFilmModel
from sqlalchemy.orm import Session


def create_film(db_session: Session, film_scheme: FilmModel):
    db_film_model: Film = Film(**film_scheme.model_dump())
    query_res = db_session.get(Film, int(film_scheme.kinopoiskId))
    if query_res is None:
        db_session.add(db_film_model)
        db_session.commit()
    return db_film_model


def create_short_film(db_session: Session, film_scheme: ShortFilmModel):
    db_short_film_model: ShortFilm = ShortFilm(**film_scheme.model_dump())
    query_res = db_session.get(ShortFilm, int(film_scheme.filmId))
    if query_res is None:
        db_session.add(db_short_film_model)
        db_session.commit()
    return db_short_film_model
