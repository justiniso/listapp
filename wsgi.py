# -*- coding: utf-8 -*-

import sys

import os
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

__all__ = ['api_app']

# Add this path; note this MUST go above project imports
sys.path.append(os.path.dirname(__file__))

# Cannot import app without this:
sys.path.insert(0, os.path.dirname(__file__))

# These imports must be below all path modifications
from src.api import api_app


application = DispatcherMiddleware(api_app, {})

# Dev mode
if __name__ == '__main__':
    from src.api.model import db, Base

    api_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/listapp'

    with api_app.app_context():

        Base.metadata.create_all(db.engine)
        # db.create_all(app=api_app)

    # Activate debug mode for dev
    api_app.debug = True

    run_simple('127.0.0.1', 5000, application, use_reloader=True, use_debugger=True, threaded=True)