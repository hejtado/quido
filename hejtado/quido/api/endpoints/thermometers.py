#!/usr/bin/env python
#
#  Copyright (C) 2019 AlfaWolf s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@alfawolf.eu
#  http://www.alfawolf.eu
#
#
import logging

from hejtado.quido.app import api


log = logging.getLogger(__name__)

ns = api.namespace('quido/thermometers', description='Operations with Quido thermometer(s)')



