#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x19-peer_connection.json
# Device ID:          0x19
# Device Name:        connection
# Timestamp:          02/21/2019 @ 00:09:09.868642 (UTC)

from enum import IntEnum


__all__ = ['BleCentralStatesEnum']


class CommandsEnum(IntEnum):
    set_bluetooth_device_name = 0x03
    get_bluetooth_device_name = 0x04


class BleCentralStatesEnum(IntEnum):
    ''' '''
    not_yet_initialized = 0  #: 
    disconnected = 1  #: 
    scanning = 2  #: 
    connecting = 3  #: 
    reconnecting = 4  #: 
    connected = 5  #: 
    disconnecting = 6  #: 
    configuring = 7  #: 
