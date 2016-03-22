#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'lzhao'

from sqlalchemy import create_engine, Column, Integer, String

engine = create_engine("postgresql+psycopg2://lzhao:@localhost:5432/sqlalchemy",
                       connect_args={'client_encoding': 'utf8',
                                     'echo': True})

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    password = Column(String(10))

    def __repr__(self):
        return "<User(name=%s, name=%s, password=%s)>" % (self.name, self.name, self.password)


