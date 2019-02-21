#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x1A-user_io.json
# Device ID:          0x1A
# Device Name:        io
# Timestamp:          02/21/2019 @ 00:09:09.859072 (UTC)

from spheroboros.common.commands.io import CommandsEnum
from spheroboros.common.devices import DevicesEnum
from spheroboros.common.parameter import Parameter


def set_all_leds_with_32_bit_mask(self, led_group, led_brightness_values, target, timeout=None):
    return self._dal.send_command(
        DevicesEnum.io,
        CommandsEnum.set_all_leds_with_32_bit_mask,
        target,
        timeout,
        inputs=[
            Parameter(
                name='ledGroup',
                data_type='uint32_t',
                index=0,
                value=led_group,
                size=1
            ),
            Parameter(
                name='ledBrightnessValues',
                data_type='uint8_t',
                index=1,
                value=led_brightness_values,
                size=32
            ),
        ],
    )


def enable_usb_status_async(self, enable, target, timeout=None):
    return self._dal.send_command(
        DevicesEnum.io,
        CommandsEnum.enable_usb_status_async,
        target,
        timeout,
        inputs=[
            Parameter(
                name='enable',
                data_type='bool',
                index=0,
                value=enable,
                size=1
            ),
        ],
    )


def on_usb_connection_status_notify(self, target, handler=None, timeout=None):
    self._dal.on_command(
        DevicesEnum.io,
        CommandsEnum.usb_connection_status_notify,
        target,
        handler,
        timeout,
        outputs=[
            Parameter(
                name='usbConnectionStatus',
                data_type='uint8_t',
                index=0,
                size=1
            ),
        ],
    )


def get_usb_connection_status(self, target, timeout=None):
    return self._dal.send_command(
        DevicesEnum.io,
        CommandsEnum.get_usb_connection_status,
        target,
        timeout,
        outputs=[
            Parameter(
                name='usbConnectionStatus',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ],
    )
