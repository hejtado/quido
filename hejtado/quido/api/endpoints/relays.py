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
ns = api.namespace('quido/relays', description='Operations with Quido relays')
relays = api.model('Quido Relays', {
    'id': fields.Integer(readonly=True, description='The Quido Relay unique identifier'),
    'name': fields.String(required=True, description='The relay name')
})

# TODO Get the description automatically from Quido box
QUIDO_RELAYS = {1: 'prodluzovacka',
                2: 'reset-ling',
                3: 'tepla-voda'}

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
