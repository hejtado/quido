#!/usr/bin/env python
#
#  Copyright (C) 2019 AlfaWolf s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@alfawolf.eu
#  http://www.alfawolf.eu
#
#
import logging

from flask_restplus import Resource, fields

from hejtado.quido.api import api

log = logging.getLogger(__name__)
ns = api.namespace('quido/thermometers', description='Operations with Quido thermometer(s)')
thermometers = api.model('Quido Thermometer', {
    'id': fields.Integer(readonly=True, description='The Quido Thermometer unique identifier'),
    'name': fields.String(required=True, description='The thermometer name')
})


@ns.route('/')
class QuidoThermometer(Resource):
    """
    List the available Quido thermometers
    """

    @ns.doc('list_quido_thermometers')
    @ns.marshal_list_with(thermometers)
    def get(self):
        """
        Get all thermometers and return them as list of dictionaries
        :return: List of available thermometers
        """
        return [{'id': 1, 'name': 'boiler'}]
