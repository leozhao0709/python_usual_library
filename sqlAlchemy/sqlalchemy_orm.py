#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

__author__ = 'lzhao'

# print sqlalchemy.__version__
engine = create_engine("postgresql://lzhao:@localhost:5432/sqlalchemy_tutorial", paramstyle='format', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    fullname = Column(String)
    password = Column(String, nullable=False)

    def __repr__(self):
        return "<User(name = %s, fullname = %s, password = %s)>" % (self.name, self.fullname, self.password)


# Base.metadata.create_all(engine)

# ed_user = User(name='ed', fullname='Ed Jones', password='edpassword')
#
# print ed_user

Session = sessionmaker(bind=engine)
session = Session()
# session.add(ed_user)
# our_user = session.query(User).filter_by(name='ed').first()
#
# session.add_all([
#     User(name='wendy', fullname='Wendy Williams', password="foobar"),
#     User(name='mary', fullname='Mary Contrary', password="xxg527"),
#     User(name='fred', fullname='Fred Flinstone', password="blah")
# ])
#
# session.commit()

# print session.query(User).all()

# for row in session.query(User).order_by(User.id):
#     print row
#
# for row in session.query(User).filter(User.name.in_(['ed', 'wendy'])):
#     print row

# for row in session.query(User).filter(~User.name.in_(['ed', 'wendy', 'jack'])):
#     print row

# print session.query(User).filter(User.name == 'ed').count()

# from sqlalchemy import and_, or_
#
# for row in session.query(User).filter(and_(User.name == 'ed', User.fullname == 'Ed Jones')):
#     print row
# for row in session.query(User).filter(or_(User.name == 'ed', User.name == 'wendy')):
#     print row

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", backref=backref('addresses', order_by=id))

    def __repr__(self):
        return "<Address(email_address=%s)>" % self.email_address


# Base.metadata.create_all(engine)

# jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
# jack.addresses = [
#     Address(email_address='jack@google.com'),
#     Address(email_address='j25@yahoo.com')
# ]
# session.add(jack)
# session.commit()

for u, a in session.query(User, Address).filter(User.id == Address.user_id).all():
    print u, a
