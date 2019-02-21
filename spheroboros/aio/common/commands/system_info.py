#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x11-system_info.json
# Device ID:          0x11
# Device Name:        system_info
# Timestamp:          02/21/2019 @ 00:09:09.869475 (UTC)

from spheroboros.common.commands.system_info import CommandsEnum
from spheroboros.common.devices import DevicesEnum
from spheroboros.common.parameter import Parameter


async def get_main_application_version(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_main_application_version,
        target,
        timeout,
        outputs=[
            Parameter(
                name='major',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
            Parameter(
                name='minor',
                data_type='uint16_t',
                index=1,
                size=1,
            ),
            Parameter(
                name='revision',
                data_type='uint16_t',
                index=2,
                size=1,
            ),
        ],
    )


async def get_bootloader_version(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_bootloader_version,
        target,
        timeout,
        outputs=[
            Parameter(
                name='major',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
            Parameter(
                name='minor',
                data_type='uint16_t',
                index=1,
                size=1,
            ),
            Parameter(
                name='revision',
                data_type='uint16_t',
                index=2,
                size=1,
            ),
        ],
    )


async def get_board_revision(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_board_revision,
        target,
        timeout,
        outputs=[
            Parameter(
                name='revision',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ],
    )


async def get_mac_address(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_mac_address,
        target,
        timeout,
        outputs=[
            Parameter(
                name='macAddress',
                data_type='std::string',
                index=0,
                size=1,
            ),
        ],
    )


async def get_nordic_temperature(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_nordic_temperature,
        target,
        timeout,
        outputs=[
            Parameter(
                name='temperature',
                data_type='int32_t',
                index=0,
                size=2,
            ),
        ],
    )


async def get_stats_id(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_stats_id,
        target,
        timeout,
        outputs=[
            Parameter(
                name='statsId',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
        ],
    )


async def get_processor_name(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_processor_name,
        target,
        timeout,
        outputs=[
            Parameter(
                name='name',
                data_type='std::string',
                index=0,
                size=1,
            ),
        ],
    )


async def get_boot_reason(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_boot_reason,
        target,
        timeout,
        outputs=[
            Parameter(
                name='reason',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ],
    )


async def get_last_error_info(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_last_error_info,
        target,
        timeout,
        outputs=[
            Parameter(
                name='fileName',
                data_type='uint8_t',
                index=0,
                size=32,
            ),
            Parameter(
                name='lineNumber',
                data_type='uint16_t',
                index=1,
                size=1,
            ),
            Parameter(
                name='data',
                data_type='uint8_t',
                index=2,
                size=12,
            ),
        ],
    )


async def get_manufacturing_date(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_manufacturing_date,
        target,
        timeout,
        outputs=[
            Parameter(
                name='year',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
            Parameter(
                name='month',
                data_type='uint8_t',
                index=1,
                size=1,
            ),
            Parameter(
                name='day',
                data_type='uint8_t',
                index=2,
                size=1,
            ),
        ],
    )


async def get_sku(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_sku,
        target,
        timeout,
        outputs=[
            Parameter(
                name='sku',
                data_type='std::string',
                index=0,
                size=1,
            ),
        ],
    )
