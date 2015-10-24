# -*- coding: utf-8 -*-

from flask_restful import Resource, abort

from . import Base
from src.api.database import db


class Item(Base):

    __tablename__ = 'item'

    __attributes__ = ['id', 'votes', 'url', 'list_id']

    id = db.Column(db.Integer(), primary_key=True)
    votes = db.Column(db.Integer(), default=0)
    url = db.Column(db.String(2080))
    list_id = db.Column('List', db.Integer(), db.ForeignKey('list.id'))

    def increment_vote(self, count=1):
        # Atomic counter increment
        # http://stackoverflow.com/questions/2334824/how-to-increase-a-counter-in-sqlalchemy
        self.votes = Item.votes + int(count)


class ItemResource(Resource):

    def get(self, item_id):
        item = Item.query.get(item_id)

        if item is None:
            abort(404)

        return item.serialize()


class ItemsResource(Resource):
    pass