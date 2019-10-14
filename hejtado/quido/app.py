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

from hejtado.quido import app, blueprint
from hejtado.quido.api import api
from hejtado.quido.settings import *
from hejtado.quido.api.endpoints.relays import ns as relays_namespace
from hejtado.quido.api.endpoints.thermometers import ns as thermometers_namespace
from hejtado.quido.settings import QUIDO_API_VERSION


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
    flask_app.config['ENV'] = FLASK_ENV


def initialize_app(flask_app):
    """
    Initialize Flask app
    :param flask_app: Flask aplication instance
    :return: None
    """
    configure_app(flask_app)
    api.init_app(blueprint)
    api.add_namespace(relays_namespace)
    api.add_namespace(thermometers_namespace)
    flask_app.register_blueprint(blueprint)


def main():
    """
    Main function
    :return:    Flask app instance
    """

    initialize_app(app)
    log.info('Starting server at http://{}/api/{}'.format(app.config['SERVER_NAME'], QUIDO_API_VERSION))
    return app.run(debug=FLASK_DEBUG)


if __name__ == "__main__":
    main()
