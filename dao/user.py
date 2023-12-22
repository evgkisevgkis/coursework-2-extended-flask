from dao.models.user import User


class UserDAO:
    """DAO for users, authentication, creating and updating"""

    def __init__(self, session):
        self.session = session

    def get_user_by_email(self, email):
        return self.session.query(User).filter(User.email == email).one()

    def create(self, data):
        new_user = User(**data)
        try:
            self.session.add(new_user)
            self.session.commit()
            return new_user
        except Exception as e:
            return e

    def update(self, data):
        user = self.get_user_by_email(data.get('email'))
        user.name = data.get('name')
        user.surname = data.get('surname')
        user.favorite_genre = data.get('favorite_genre')
        self.session.add(user)
        self.session.commit()
        return user

    def update_password(self, email, new_password):
        user = self.get_user_by_email(email)
        user.password = new_password
        self.session.add(user)
        self.session.commit()
        return user
