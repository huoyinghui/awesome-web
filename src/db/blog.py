# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Text, ForeignKey
from sqlalchemy.orm import relationship, backref
from base import Base


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    summary = Column(String)
    created_at = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="blogs")
    comments = relationship("Comment")


if __name__ == '__main__':
    pass
