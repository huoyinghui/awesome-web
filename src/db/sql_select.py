# 1 - imports
from base import Session, engine, Base
from user import User
from blog import Blog


# 2 - generate database schema
Base.metadata.create_all(engine)

# 2.1 create user
# user_list = [User(fake.name(), fake.email(), fake.word()) for i in range(10)]

# # 4 - create movies
# bourne_identity = Movie("The Bourne Identity", date(2002, 10, 11))
# furious_7 = Movie("Furious 7", date(2015, 4, 2))
# pain_and_gain = Movie("Pain & Gain", date(2013, 8, 23))
#
# # 5 - creates actors
# matt_damon = Actor("Matt Damon", date(1970, 10, 8))
# dwayne_johnson = Actor("Dwayne Johnson", date(1972, 5, 2))
# mark_wahlberg = Actor("Mark Wahlberg", date(1971, 6, 5))
#
#
# # 6 - add actors to movies
# bourne_identity.actors = [matt_damon]
# furious_7.actors = [dwayne_johnson]
# pain_and_gain.actors = [dwayne_johnson, mark_wahlberg]
#
#
# # 7 - add contact details to actors
# matt_contact = ContactDetails("415 555 2671", "Burbank, CA", matt_damon)
# dwayne_contact = ContactDetails("423 555 5623", "Glendale, CA", dwayne_johnson)
# dwayne_contact_2 = ContactDetails("421 444 2323", "West Hollywood, CA", dwayne_johnson)
# mark_contact = ContactDetails("421 333 9428", "Glendale, CA", mark_wahlberg)
#
#
# # 8 - create stuntmen
# matt_stuntman = Stuntman("John Doe", True, matt_damon)
# dwayne_stuntman = Stuntman("John Roe", True, dwayne_johnson)
# mark_stuntman = Stuntman("Richard Roe", True, mark_wahlberg)

if __name__ == '__main__':
    # 3 - create a new session
    session = Session()
    # 9 - persists data
    # session.add_all(user_list)
    # for row in session.query(User, User.name).all():
    #     print(row.User.id, row.User.email, row.User.password, row.User.created_at)

    # for row in session.query(User).filter(User.name == 'hyh').order_by(User.id):
    user_list = []
    for row in session.query(User).filter(User.name != 'hyh').order_by(User.id):
        print(row.blog)
        user_list.append(row)

    user_cnt = session.query(User).filter(User.name != 'hyh').order_by(User.id).count()
    print(user_cnt)

    blog = Blog()
    for row in session.query(Blog).order_by(Blog.id):
        print(row)

    # session.add(bourne_identity)
    # session.add(furious_7)
    # session.add(pain_and_gain)
    #
    # session.add(matt_contact)
    # session.add(dwayne_contact)
    # session.add(dwayne_contact_2)
    # session.add(mark_contact)
    #
    # session.add(matt_stuntman)
    # session.add(dwayne_stuntman)
    # session.add(mark_stuntman)

    # 10 - commit and close session
    session.commit()
    session.close()