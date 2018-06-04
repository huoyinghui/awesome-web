# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Text, ForeignKey
from sqlalchemy.orm import relationship, backref
from base import Base


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(Text)
    created_at = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    # user = relationship("User", backref=backref("comments"))
    user = relationship("User", back_populates="comments")
    blog_id = Column(Integer, ForeignKey('blogs.id'))
    # blog = relationship("Blog", backref=backref("comments"))
    blog = relationship("Blog", back_populates="comments")


if __name__ == '__main__':
    pass
