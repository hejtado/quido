#!/usr/bin/env python
#
#  Copyright (C) 2019 AlfaWolf s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@alfawolf.eu
#  http://www.alfawolf.eu
#
#
from flask import Flask, Blueprint

from hejtado.quido.settings import QUIDO_API_VERSION

# Set Flask app
app = Flask(__name__)
url_prefix = "/api/{}".format(QUIDO_API_VERSION)
blueprint = Blueprint('api', __name__, url_prefix=url_prefix)
