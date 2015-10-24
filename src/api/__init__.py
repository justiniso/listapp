# -*- coding: utf-8 -*-

from flask_restful import Api

from .database import db
from .model.item import Item, ItemResource, ItemsResource
from .model.list import List, ListResource, ListsResource
from src import appfactory

__all__ = ['Item', 'List']


def _create_app():

    app = appfactory.create_app(__name__)

    db.init_app(app)

    api = Api(app)
    api.add_resource(ItemsResource, '/item')
    api.add_resource(ItemResource, '/item/<int:item_id>')
    api.add_resource(ListsResource, '/list')
    api.add_resource(ListResource, '/list/<int:list_id>')

    return app


api_app = _create_app()
