#!/usr/bin/env python
#
#  Copyright (C) 2019 AlfaWolf s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@alfawolf.eu
#  http://www.alfawolf.eu
#
#
import logging

from pysnmp.hlapi import *

from hejtado.quido.settings import QUIDO_IP

log = logging.getLogger(__name__)


class Quido:
    """Handle communication with Quido box"""

    def __init__(self):
        self.quido_ip = QUIDO_IP

    def __create_data_structure(self):
        """Create datastructure to hold Quido values"""

    def get_boiler_temperature(self):
        """
        Get the temperature of thermometer connected to the Quido
        :return: Boiler temperature
        """
        oid = '1.3.6.1.4.1.18248.16.1.1.0'
        log.debug("get_boiler_temperature sends oid {}".format(oid))
        boiler_temperature = self.__snmp_get(oid)
        log.debug("get_boiler_temperature received temperature string {}".format(boiler_temperature))
        boiler_temperature = float(self.__select_return_value(boiler_temperature) / 10)

        # In case of negative temperature, please see Modbus and pyminimalmodbus documentation
        if boiler_temperature > 6000:
            boiler_temperature = boiler_temperature - 6553.6
        return boiler_temperature

    def get_relay_status(self, relay_id):
        """
        Return the relay status
        :param relay_id: Integer with relay ID
        :return: Return 0/1 based on relay state
        """

        oid = "1.3.6.1.4.1.18248.16.3.1.1.1." + str(relay_id)
        log.debug("get_relay_status sends oid {}".format(oid))
        relay_state = self.__snmp_get(oid)
        log.debug("get_relay_status received relay_state {}".format(relay_state))
        relay_state = self.__select_return_value(relay_state)

        return relay_state

    def get_relay_name(self, relay_id):
        """
        Return the description of the relay
        :param relay_id: Integer with relay ID
        :return: Return string with relay description
        """

        oid = "1.3.6.1.4.1.18248.16.3.1.1.2." + str(relay_id)
        log.debug("get_relay_name sends oid {}".format(oid))
        relay_name = self.__snmp_get(oid)
        log.debug("get_relay_status received relay_state {}".format(relay_name))
        relay_name = self.__select_return_value(relay_name)

        return relay_name

    def get_relay_type(self, relay_id):
        """
        Return the type of the relay (static/pulse)
        :param relay_id: Integer with relay ID
        :return: Return string with relay type
        """

        oid = "1.3.6.1.4.1.18248.16.3.1.1.3." + str(relay_id)
        log.debug("get_relay_name sends oid {}".format(oid))
        relay_type = self.__snmp_get(oid)
        log.debug("get_relay_type received relay_state {}".format(relay_type))
        relay_type = int(self.__select_return_value(relay_type))
        if relay_type == 1:
            relay_type = 'static'
        elif relay_type > 1:
            relay_type = 'pulse'
        else:
            relay_type = 'unknown'

        return relay_type

    def set_relay(self, relay_id, desired_state):
        """Set the status of the relay"""

        oid = "1.3.6.1.4.1.18248.16.3.1.1.1." + str(relay_id)
        desired_state_value = 0

        log.info("set_relay received input parameters: {} {}".format(relay_id, desired_state))
        if desired_state == 'on':
            desired_state_value = 1
        log.debug("set_relay sends oid {}".format(oid))
        self.__snmp_set(oid, desired_state_value)
        return True

    @staticmethod
    def __select_return_value(snmp_string):
        """
        Select and return SNMP value from input string
        :param snmp_string: Input string
        :return: Return splitted string
        """
        log.debug("__select_return_value returns: {}".format(snmp_string.rsplit("= ")[1]))

        return snmp_string.rsplit("= ")[1]

    def __snmp_get(self, oid):
        """Get Quido Relay information using SNMP"""
        data = next(getCmd(SnmpEngine(),
                           CommunityData('private', mpModel=0),
                           UdpTransportTarget((self.quido_ip, 161)),
                           ContextData(),
                           ObjectType(ObjectIdentity(oid)))
                    )
        log.debug("__snmp_get returns: {}".format(data[3][0].prettyPrint()))

        return data[3][0].prettyPrint()

    def __snmp_set(self, oid, desired_state_value):
        """
        Set SNMP value on relay
        :param oid: OID string
        :return: return SNMP output string
        """
        data = next(
            setCmd(SnmpEngine(),
                   CommunityData('private', mpModel=0),
                   UdpTransportTarget((self.quido_ip, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity(oid), Integer(int(desired_state_value))))
        )
        log.debug("__snmp_set returns {}".format(data[3][0].prettyPrint()))

        return data[3][0].prettyPrint()
