# 1 - imports
from datetime import date

from base import Session, engine, Base
# from actor import Actor
# from contact_details import ContactDetails
# from movie import Movie
# from stuntman import Stuntman
from user import User
from blog import Blog
from comment import Comment
# from address import Address
from faker import Faker
from sqlalchemy.orm import relationship


fake = Faker()
# 2 - generate database schema
Base.metadata.create_all(engine)

# 2.1 create user
user_list = [User(name=fake.name(), email=fake.email(), password=fake.word(), admin=True, image='', created_at=fake.date()) for i in range(10)]
# addr_list = [Address(email_address=fake.email()) for i in range(3)]
blog_list = [Blog(title='aa:{}'.format(i), summary=fake.text(), created_at=fake.date()) for i in range(10)]
# user_list[0].addresses = addr_list
comment_list = [Comment(name='aa:{}'.format(i), content=fake.text(), created_at=fake.date()) for i in range(10)]

for index in range(len(comment_list)):
    comment_list[index].user = user_list[index]

u = user_list[0]
u.comments = [comment_list[0]]


blog_list[0].comments = comment_list
blog_list[0].user = u


if __name__ == '__main__':
    # 3 - create a new session
    session = Session()
    session.add(blog_list[0])
    session.commit()
    session.close()