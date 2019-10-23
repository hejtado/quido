#!/usr/bin/env python
#
#  Copyright (C) 2019 AlfaWolf s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@alfawolf.eu
#  http://www.alfawolf.eu
#
#
from flask_restplus import Api

from hejtado.quido import app

# TODO Implement app/api version from variable, not statically
# Set Flask API
api = Api(app, version='0.1', title='Hejtado Quido API',
          description='API that gives access to the Quido hardware box')
