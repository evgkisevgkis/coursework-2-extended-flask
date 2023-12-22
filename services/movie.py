from dao.movie import MovieDAO


class MovieService:
    """Service for movies, CRUD operations"""
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, filters):
        return self.dao.get_all(filters)

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        return self.dao.update(data)

    def delete(self, mid):
        return self.dao.delete(mid)
