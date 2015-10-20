# -*- coding: utf-8 -*-

from . import Base
from src.api.database import db


class Item(Base):

    __tablename__ = 'item'

    id = db.Column(db.Integer(), primary_key=True)
    votes = db.Column(db.Integer(), default=0)
    url = db.Column(db.String(2080))
    list_id = db.relationship('List', db.Integer(), db.ForeignKey('list.id'),
                              backref=db.backref('item', lazy='dynamic'))

    def increment_vote(self, count=1):
        # Atomic counter increment
        # http://stackoverflow.com/questions/2334824/how-to-increase-a-counter-in-sqlalchemy
        self.votes = Item.votes + int(count)
