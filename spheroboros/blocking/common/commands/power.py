#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x13-power.json
# Device ID:          0x13
# Device Name:        power
# Timestamp:          02/21/2019 @ 00:09:09.866006 (UTC)

from spheroboros.common.commands.power import CommandsEnum
from spheroboros.common.devices import DevicesEnum
from spheroboros.common.parameter import Parameter


def enter_deep_sleep(self, seconds_until_deep_sleep, target, timeout=None):
    return self._dal.send_command(
        DevicesEnum.power,
        CommandsEnum.enter_deep_sleep,
        target,
        timeout,
        inputs=[
            Parameter(
                name='secondsUntilDeepSleep',
                data_type='uint8_t',
                index=0,
                value=seconds_until_deep_sleep,
                size=1
            ),
        ],
    )


def enter_soft_sleep(self, target, timeout=None):
    return self._dal.send_command(
        DevicesEnum.power,
        CommandsEnum.enter_soft_sleep,
        target,
        timeout,
    )


def wake(self, target, timeout=None):
    return self._dal.send_command(
        DevicesEnum.power,
        CommandsEnum.wake,
        target,
        timeout,
    )


def get_battery_percentage(self, target, timeout=None):
    return self._dal.send_command(
        DevicesEnum.power,
        CommandsEnum.get_battery_percentage,
        target,
        timeout,
        outputs=[
            Parameter(
                name='percentage',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ],
    )


def get_battery_voltage_state(self, target, timeout=None):
    return self._dal.send_command(
        DevicesEnum.power,
        CommandsEnum.get_battery_voltage_state,
        target,
        timeout,
        outputs=[
            Parameter(
                name='state',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ],
    )


def on_will_sleep_notify(self, target, handler=None, timeout=None):
    self._dal.on_command(
        DevicesEnum.power,
        CommandsEnum.will_sleep_notify,
        target,
        handler,
        timeout,
    )


def on_did_sleep_notify(self, target, handler=None, timeout=None):
    self._dal.on_command(
        DevicesEnum.power,
        CommandsEnum.did_sleep_notify,
        target,
        handler,
        timeout,
    )


def enable_battery_voltage_state_change_notify(self, is_enabled, target, timeout=None):
    return self._dal.send_command(
        DevicesEnum.power,
        CommandsEnum.enable_battery_voltage_state_change_notify,
        target,
        timeout,
        inputs=[
            Parameter(
                name='isEnabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    )


def on_battery_voltage_state_change_notify(self, target, handler=None, timeout=None):
    self._dal.on_command(
        DevicesEnum.power,
        CommandsEnum.battery_voltage_state_change_notify,
        target,
        handler,
        timeout,
        outputs=[
            Parameter(
                name='state',
                data_type='uint8_t',
                index=0,
                size=1
            ),
        ],
    )
