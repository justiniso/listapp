# -*- coding: utf-8 -*-

from . import Base
from src.api.database import db


class List(Base):

    __tablename__ = 'list'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    create_date = db.Column(db.DateTime())
    publish_date = db.Column(db.DateTime())
    delete_date = db.Column(db.DateTime())
