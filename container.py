from dao.genre import GenreDAO
from dao.director import DirectorDAO
from dao.movie import MovieDAO
from dao.user import UserDAO
from services.genre import GenreService
from services.director import DirectorService
from services.movie import MovieService
from services.user import UserService
from setup_db import db

# DAOs

genre_dao = GenreDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)

# Services

genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
