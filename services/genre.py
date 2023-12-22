from dao.genre import GenreDAO


class GenreService:
    """Service for genres, CRUD operations"""
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        return self.dao.update(data)

    def delete(self, gid):
        return self.dao.delete(gid)
