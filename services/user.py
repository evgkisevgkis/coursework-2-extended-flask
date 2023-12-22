from dao.user import UserDAO


class UserService:
    """Service for users"""
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_user_by_email(self, email):
        return self.dao.get_user_by_email(email)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        return self.dao.update(data)

    def update_password(self, email, password):
        return self.dao.update_password(email, password)
