# -*- coding: utf-8 -*-

from flask_restful import Resource, abort, request, fields, marshal_with

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


public_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'publish_date': fields.DateTime
}


class ListResource(Resource):

    @marshal_with(public_fields)
    def get(self, list_id):
        list_ = List.query.get(list_id)

        if list_ is None:
            abort(404)

        return list_

    @marshal_with(public_fields)
    def put(self, list_id):
        list_ = List.query.get(list_id)

        # TODO: update

        return list_


class ListsResource(Resource):

    @marshal_with(public_fields)
    def post(self):
        data = request.get_json()
        list_ = List()
        db.session.add(list_)
        db.session.commit()

        return list_

    def get(self):
        """Query endpoint"""
        raise NotImplementedError