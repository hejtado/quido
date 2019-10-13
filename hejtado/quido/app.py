#!/usr/bin/env python
#
#  Copyright (C) 2019 AlfaWolf s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@alfawolf.eu
#  http://www.alfawolf.eu
#
#

import os
import logging.config

from flask import Flask, Blueprint
from flask_restplus import Api
from hejtado.quido.settings import *
# from hejtado.quido.api.endpoints.relays import ns as relays_namespace
# from hejtado.quido.api.endpoints.thermometers import ns as thermometers_namespace

# Set Flask API
api = Api(version='0.1', title='Hejtado Quido API',
          description='API that gives access to the Quido hardware box')

# Set Flask app
app = Flask(__name__)
# Set logging
logging_conf_path = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    """
    Configure Flask app
    :param flask_app: Flask app instance
    :return: None
    """

    server_name = FLASK_SERVER + ":" + str(FLASK_PORT)
    flask_app.config['SERVER_NAME'] = server_name
    flask_app.config['PORT'] = FLASK_PORT


def initialize_app(flask_app):
    """
    Initialize Flask app

    :param flask_app: Flask aplication instance
    :return: None
    """
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    relays_namespace = api.namespace('quido/relays', description='Operations with Quido relays')
    thermometers_namespace = api.namespace('quido/thermometers', description='Operations with Quido thermometer(s)')
    api.add_namespace(relays_namespace)
    api.add_namespace(thermometers_namespace)


def main():
    """
    Main function
    :return:    Flask app instance
    """

    initialize_app(app)
    log.info('Starting server at http://{}/api/'.format(app.config['SERVER_NAME']))
    return app.run(debug=FLASK_DEBUG)


if __name__ == "__main__":
    main()
