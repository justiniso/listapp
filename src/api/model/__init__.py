# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base

from src.api.database import db


class Base(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = db.Column(db.Integer(), primary_key=True)


Base = declarative_base(cls=Base)