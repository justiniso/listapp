# -*- coding: utf-8 -*-

from flask_restful import Resource, abort, request, fields, marshal_with, reqparse

from . import Base, item
from sqlalchemy.orm import relationship
from src.api.database import db


class Post(Base):

    __tablename__ = 'post'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    slug = db.Column(db.String(255))
    publish_date = db.Column(db.DateTime())

    items = relationship('Item')

    def __init__(self, data=None):
        if data is not None:
            self.load(data)

    def load(self, data):
        self.id = data.get('id')
        self.title = data.get('title')
        self.description = data.get('description')
        self.slug = data.get('slug')

public_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'publish_date': fields.DateTime,
    'items': fields.Nested(item.public_fields)
}


class PostResource(Resource):

    @marshal_with(public_fields)
    def get(self, list_id):
        post = Post.query.get(list_id)

        if post is None:
            abort(404)

        return post

    @marshal_with(public_fields)
    def put(self, list_id):
        post = Post.query.get(list_id)

        # TODO: update

        return post


class PostsResource(Resource):

    @marshal_with(public_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=True)

        data = parser.parse_args()

        pst = Post(data)
        db.session.add(pst)
        db.session.commit()

        return pst

    def get(self):
        """Query endpoint"""
        raise NotImplementedError