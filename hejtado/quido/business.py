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

    def get_temperature(self):
        """Get the temperature of thermometer connected to the Quido"""
        temperature_obj = self.__snmp_get('1.3.6.1.4.1.18248.16.1.1.0')
        temperature = float(temperature_obj[1][1]) / 10
        # In case of negative temperature, please see Modbus and pyminimalmodbus documentation
        if temperature > 6000:
            temperature = temperature - 6553.6
        return temperature

    def get_relay_status(self, relayID):
        """
        Return the relay status
        :param relayID: Integer with relay ID
        :return: Return 0/1 based on relay state
        """

        oid = "1.3.6.1.4.1.18248.16.3.1.1.1." + str(relayID)
        log.debug("get_relay_status sends oid {}".format(oid))
        relay_state = self.__snmp_get(oid)
        return relay_state

    def set_relay(self, relayID, desired_state):
        """Set the status of the relay"""

        oid = "1.3.6.1.4.1.18248.16.3.1.1.1." + str(relayID)
        desired_state_value = 0

        if desired_state == 'on':
            desired_state_value = 1

        errorIndication, errorStatus, errorIndex, varBinds = next(
            setCmd(SnmpEngine(),
                   CommunityData('private', mpModel=0),
                   UdpTransportTarget((self.quido_ip, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity(oid), Integer(int(desired_state_value))))
        )
        if errorIndication:
            return False
        else:
            return True

    def __snmp_get(self, oid):
        """Get Quido Relay information using SNMP"""
        data = next(getCmd(SnmpEngine(),
                        CommunityData('private', mpModel=0),
                        UdpTransportTarget((self.quido_ip, 161)),
                        ContextData(),
                        ObjectType(ObjectIdentity(oid)))
                    )
        log.debug("__snmp_get returns: {}".format(data[3][0].prettyPrint()[-1]))
        return data[3][0].prettyPrint()[-1]

    def __snmp_set(self):
        pass
