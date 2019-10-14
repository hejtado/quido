#!/usr/bin/env python
#
#  Copyright (C) 2019 AlfaWolf s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@alfawolf.eu
#  http://www.alfawolf.eu
#
#
from flask_restplus import Api

# Set Flask API
api = Api(version='0.1', title='Hejtado Quido API',
          description='API that gives access to the Quido hardware box')
