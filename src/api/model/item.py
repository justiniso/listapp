# -*- coding: utf-8 -*-

from flask_restful import Resource, abort, reqparse, marshal_with, fields

from . import Base
from src.api.database import db


class Item(Base):

    __tablename__ = 'item'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    caption = db.Column(db.String(2080))
    votes = db.Column(db.Integer(), default=0)
    url = db.Column(db.String(2080))
    thumbnail_url = db.Column(db.String(2080))

    post_id = db.Column('Post', db.Integer(), db.ForeignKey('post.id'))

    def __init__(self, data=None):
        if data is not None:
            self.load(data)

    def load(self, data):
        self.id = data.get('id')
        self.title = data.get('title')
        self.caption = data.get('caption')
        self.url = data.get('url')
        self.thumbnail_url = data.get('thumbnail_url')
        self.post_id = data.get('post_id')

    def increment_vote(self, count=1):
        # Atomic counter increment
        # http://stackoverflow.com/questions/2334824/how-to-increase-a-counter-in-sqlalchemy
        self.votes = Item.votes + int(count)

public_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'caption': fields.String,
    'votes': fields.Integer,
    'url': fields.String,
    'thumbnail_url': fields.String,
    'post_id': fields.Integer
}


class ItemResource(Resource):

    @marshal_with(public_fields)
    def get(self, item_id):
        item = Item.query.get(item_id)

        if item is None:
            abort(404)

        return item


class ItemsResource(Resource):

    @marshal_with(public_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('caption', type=str)
        parser.add_argument('url', type=str)
        parser.add_argument('thumbnail_url', type=str)
        parser.add_argument('post_id', type=int)

        data = parser.parse_args()

        item = Item(data)
        db.session.add(item)
        db.session.commit()

        return item