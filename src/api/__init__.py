# -*- coding: utf-8 -*-

from flask_restful import Api

from .database import db
from .model.item import Item, ItemResource, ItemsResource
from .model.post import Post, PostResource, PostsResource
from src import appfactory

__all__ = ['Item', 'Post']


def _create_app():

    app = appfactory.create_app('api')

    db.init_app(app)

    api = Api(app)
    api.add_resource(ItemsResource, '/item')
    api.add_resource(ItemResource, '/item/<int:item_id>')
    api.add_resource(PostsResource, '/post')
    api.add_resource(PostResource, '/post/<int:list_id>')

    return app


api_app = _create_app()
