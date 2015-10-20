# -*- coding: utf-8 -*-

from flask_restful import Api

from .model.item import Item
from .model.list import List
from .resources.item import ItemResource
from .resources.list import ListResource
from src import appfactory


def create_app():

    app = appfactory.create_app(__name__)

    api = Api(app)
    api.add_resource(ItemResource, '/item/<int:item_id>')
    api.add_resource(ListResource, '/list/<int:list_id>')

    return app