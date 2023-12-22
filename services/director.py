from dao.director import DirectorDAO


class DirectorService:
    """Service for directors, CRUD operations"""
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, did):
        return self.dao.get_one(did)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        return self.dao.update(data)

    def delete(self, did):
        return self.dao.delete(did)
