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
from hejtado.quido.business import Quido


log = logging.getLogger(__name__)
ns = api.namespace('quido/relays', description='Operations with Quido relays')
relays = api.model('Quido Relays', {
    'id': fields.Integer(readonly=True, description='The Quido Relay unique identifier'),
    'name': fields.String(required=True, description='The relay name'),
    'status': fields.String(required=False, description='Status of the relay (on/off)'),
    'type': fields.String(required=False, description='Type of the output')
})

# TODO Get the description automatically from Quido box
QUIDO_RELAYS = {1: 'prodluzovacka',
                2: 'reset-ling',
                3: 'tepla-voda'}

# Initialize Quido class
quido = Quido()

@ns.route('/')
class QuidoRelay(Resource):
    """
    List the available Quido relays
    """

    @ns.doc('list_quido_relays')
    @ns.marshal_list_with(relays)
    def get(self):
        """
        Get all relays and return them as list of dictionaries
        :return: List of available relays
        """
        return [{'id': id, 'name': name} for id, name in QUIDO_RELAYS.items()]

@ns.route('/<int:id>')
class QuidoRelayItem(Resource):
    """
    Get/Set the values on Quido Relay
    """

    @ns.doc('get_quido_relay_values')
    @ns.marshal_with(relays)
    def get(self, id):
        """
        Fetch a information about relay
        :param id: ID of the Relay
        :return: Return information about relay
        """
        status = int(quido.get_relay_status(id))
        if not status:
            status = "off"
        else:
            status = "on"
        log.debug("squido get relay status is \"{}\"".format(status))

        return [{'id': id, 'name': 'name', 'status': status}]
