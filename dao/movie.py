from dao.models.movie import Movie


class MovieDAO:
    """DAO for movies, CRUD operations"""
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self, filters):
        """Includes some optional filters: 'director_id', 'genre_id', 'year', 'rating'"""
        temp = self.session.query(Movie)
        if 'director_id' in filters:
            temp = temp.filter(Movie.director_id == filters.get('director_id'))
        if 'genre_id' in filters:
            temp = temp.filter(Movie.genre_id == filters.get('genre_id'))
        if 'year' in filters:
            temp = temp.filter(Movie.year == filters.get('year'))
        if 'rating' in filters:
            temp = temp.filter(Movie.rating >= filters.get('rating'))
        return temp.all()

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, data):
        movie = self.get_one(data.get('id'))
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
        return movie
