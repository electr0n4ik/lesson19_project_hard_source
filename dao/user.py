from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def get_all(self):
        # А еще можно сделать так, вместо всех методов get_by_*
        # t = self.session.query(User)
        # if "director_id" in filters:
        #     t = t.filter(User.director_id == filters.get("director_id"))
        # if "genre_id" in filters:
        #     t = t.filter(User.genre_id == filters.get("genre_id"))
        # if "year" in filters:
        #     t = t.filter(User.year == filters.get("year"))
        # return t.all()
        return self.session.query(User).all()


    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        user.username = user_d.get("username")
        user.password = user_d.get("password")
        user.role = user_d.get("role")

        self.session.add(user)
        self.session.commit()
