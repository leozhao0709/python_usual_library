#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'lzhao'

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine("postgresql://lzhao:@localhost:5432/sqlalchemy_tutorial", paramstyle='format', echo=True)

MetaData = MetaData()
users = Table('users_core', MetaData,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String),
              )

addresses = Table('addresses_core', MetaData,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users_core.id')),
                  Column('email_address', String, nullable=False),
                  )

# MetaData.create_all(engine)
conn = engine.connect()

# conn.execute(users.insert(), [
#     {'name': 'jack', 'fullname': 'Jack Jones'},
#     {'name': 'wendy', 'fullname': 'Wendy Williams'}
#                               ])

# conn.execute(addresses.insert(), [
#     {'user_id': 1, 'email_address': 'jack@yahoo.com'},
#     {'user_id': 1, 'email_address': 'jack@msn.com'},
#     {'user_id': 2, 'email_address': 'www@www,org'},
#     {'user_id': 2, 'email_address': 'wendy@aol.com'},
# ])

from sqlalchemy.sql import select
s = select([users])
result = conn.execute(s)
for row in result:
    print row

s = select([users, addresses]).where(users.c.id == addresses.c.user_id)
for row in conn.execute(s):
    print row
