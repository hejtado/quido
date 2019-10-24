#!/usr/bin/env python
#
#  Copyright (C) 2019 AlfaWolf s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@alfawolf.eu
#  http://www.alfawolf.eu
#
#
import logging

from flask import request
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
        return [{'id': relay_id, 'name': name} for relay_id, name in QUIDO_RELAYS.items()]


@ns.route('/<int:relay_id>')
class QuidoRelayItem(Resource):
    """
    Get/Set the values on Quido Relay
    """

    @ns.doc('get_quido_relay_values')
    @ns.marshal_with(relays)
    def get(self, relay_id):
        """
        Fetch a information about relay
        :param relay_id: ID of the Relay
        :return: Return information about relay
        """
        status = int(quido.get_relay_status(relay_id))
        if not status:
            status = "off"
        else:
            status = "on"
        log.debug("squido get relay status is \"{}\"".format(status))
        name = quido.get_relay_name(relay_id)
        log.debug("squido get relay name is \"{}\"".format(name))
        relay_type = quido.get_relay_type(relay_id)
        log.debug("squido get relay type is \"{}\"".format(relay_type))
        relay_values = {'id': relay_id, 'name': name, 'status': status, 'type': relay_type}
        log.info("Relay values: {}".format(relay_values))

        return [relay_values]

    @ns.doc('set_quido_relays_values')
    @api.expect(relays)
    @api.response(204, 'Relay successfully updated.')
    def put(self, relay_id):
        """
        Set the new status of the relay
        :param relay_id: ID of the relay
        :return: current relay status
        """
        data = request.json
        log.debug("QuidoRelayItem put received request {}".format(data))
        status = data['status']
        quido.set_relay(relay_id, status)
        return None, 204
