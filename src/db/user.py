import hashlib
from sqlalchemy import Column, Integer, String, Boolean, Date
from datetime import date, datetime
from base import Base, encryted_salt


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    admin = Column(Boolean)
    image = Column(String)
    created_at = Column(Date)

    def __repr__(self):
        return "<User(id='{}', name='{}', email='{}', password={}, admin={}, image={}, create_at={})>".format(
            self.id, self.name, self.email, self.password, self.admin, self.image, self.created_at)

    def __init__(self, name, email, password, admin=True, image=''):
        self.name = name
        self.email = email
        self.password = encryted_salt(password)
        self.admin = admin
        self.image = image
        self.created_at = datetime.now()


if __name__ == '__main__':
    User('hyh', 'hyhlinux@163.com', 'test', admin=True, image='http://...')
    pass

