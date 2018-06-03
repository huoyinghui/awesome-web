from sqlalchemy import Column, Integer, String

from db import Base


class User(Base):
    __table__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='{}', fullname='{}', password='{}')>".format(self.name, self.fullname, self.password)


if __name__ == '__main__':
    u = User(name='ed', fullname='Ed Jones', password='edspassword')
