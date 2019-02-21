#!/usr/bin/env python3
# This file is automatically generated!
# Toy Name:           Sphero RVR
# Prefix:             RV
# Command Count:      56
# Timestamp:          02/21/2019 @ 00:09:09.873821 (UTC)

import asyncio
from spheroboros.aio.common.commands import api_and_shell
from spheroboros.aio.common.commands import system_info
from spheroboros.aio.common.commands import power
from spheroboros.aio.common.commands import drive
from spheroboros.aio.common.commands import sensor
from spheroboros.aio.common.commands import connection
from spheroboros.aio.common.commands import io
from spheroboros.aio.common.toys.async_sphero_toy import AsyncSpheroToy
from spheroboros.aio.client.dal.restful_async_dal import RestfulAsyncDal


class AsyncSpheroRvr(AsyncSpheroToy):
    def __init__(self, dal=RestfulAsyncDal(prefix='rv')):
        AsyncSpheroToy.__init__(self)
        self._dal = dal

    async def echo(self, data, target, timeout=None):
        '''echo

        :param data: 
        :type data: array of uint8_ts (up to 16)
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: data(uint8_t array)
        '''
        return await api_and_shell.echo(self, data, target, timeout=timeout)

    async def get_api_protocol_version(self, target, timeout=None):
        '''get_api_protocol_version

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: major_version(uint8_t), minor_version(uint8_t)
        '''
        return await api_and_shell.get_api_protocol_version(self, target, timeout=timeout)

    async def get_supported_dids(self, target, timeout=None):
        '''get_supported_dids

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: dids(uint8_t array)
        '''
        return await api_and_shell.get_supported_dids(self, target, timeout=timeout)

    async def get_supported_cids(self, did, target, timeout=None):
        '''get_supported_cids

        :param uint8_t did:  
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: cids(uint8_t array)
        '''
        return await api_and_shell.get_supported_cids(self, did, target, timeout=timeout)

    async def get_main_application_version(self, target, timeout=None):
        '''get_main_application_version

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: major(uint16_t), minor(uint16_t), revision(uint16_t)
        '''
        return await system_info.get_main_application_version(self, target, timeout=timeout)

    async def get_bootloader_version(self, target, timeout=None):
        '''get_bootloader_version

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: major(uint16_t), minor(uint16_t), revision(uint16_t)
        '''
        return await system_info.get_bootloader_version(self, target, timeout=timeout)

    async def get_board_revision(self, target, timeout=None):
        '''get_board_revision

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: revision(uint8_t)
        '''
        return await system_info.get_board_revision(self, target, timeout=timeout)

    async def get_mac_address(self, timeout=None):
        '''get_mac_address

        :param float timeout: maximum time to await a response

        :returns: mac_address(std::string)
        '''
        return await system_info.get_mac_address(self, target=1, timeout=timeout)

    async def get_nordic_temperature(self, timeout=None):
        '''get_nordic_temperature

        :param float timeout: maximum time to await a response

        :returns: temperature(int32_t array)
        '''
        return await system_info.get_nordic_temperature(self, target=1, timeout=timeout)

    async def get_stats_id(self, target, timeout=None):
        '''get_stats_id

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: stats_id(uint16_t)
        '''
        return await system_info.get_stats_id(self, target, timeout=timeout)

    async def get_processor_name(self, target, timeout=None):
        '''get_processor_name

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: name(std::string)
        '''
        return await system_info.get_processor_name(self, target, timeout=timeout)

    async def get_boot_reason(self, timeout=None):
        '''get_boot_reason

        :param float timeout: maximum time to await a response

        :returns: reason(uint8_t)
        '''
        return await system_info.get_boot_reason(self, target=1, timeout=timeout)

    async def get_last_error_info(self, timeout=None):
        '''get_last_error_info

        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: file_name(uint8_t array), line_number(uint16_t), data(uint8_t array)
        '''
        return await system_info.get_last_error_info(self, target=1, timeout=timeout)

    async def get_manufacturing_date(self, target, timeout=None):
        '''get_manufacturing_date

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: year(uint16_t), month(uint8_t), day(uint8_t)
        '''
        return await system_info.get_manufacturing_date(self, target, timeout=timeout)

    async def get_sku(self, target, timeout=None):
        '''get_sku

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: sku(std::string)
        '''
        return await system_info.get_sku(self, target, timeout=timeout)

    async def enter_deep_sleep(self, seconds_until_deep_sleep, timeout=None):
        '''enter_deep_sleep

        :param uint8_t seconds_until_deep_sleep:  seconds
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await power.enter_deep_sleep(self, seconds_until_deep_sleep, target=1, timeout=timeout)

    async def enter_soft_sleep(self, timeout=None):
        '''enter_soft_sleep

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await power.enter_soft_sleep(self, target=1, timeout=timeout)

    async def wake(self, timeout=None):
        '''wake

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await power.wake(self, target=1, timeout=timeout)

    async def get_battery_percentage(self, timeout=None):
        '''get_battery_percentage

        :param float timeout: maximum time to await a response

        :returns: percentage(uint8_t)
        '''
        return await power.get_battery_percentage(self, target=1, timeout=timeout)

    async def get_battery_voltage_state(self, timeout=None):
        '''get_battery_voltage_state

        :param float timeout: maximum time to await a response

        :returns: state(uint8_t)
        '''
        return await power.get_battery_voltage_state(self, target=1, timeout=timeout)

    async def on_will_sleep_notify(self, handler=None, timeout=None):
        '''will_sleep_notify

        :param coroutine handler: called asynchronously, takes form handler()
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            power.on_will_sleep_notify(self, target=1, handler=handler, timeout=timeout)
        )

    async def on_did_sleep_notify(self, handler=None, timeout=None):
        '''did_sleep_notify

        :param coroutine handler: called asynchronously, takes form handler()
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            power.on_did_sleep_notify(self, target=1, handler=handler, timeout=timeout)
        )

    async def enable_battery_voltage_state_change_notify(self, is_enabled, timeout=None):
        '''enable_battery_voltage_state_change_notify

        :param bool is_enabled:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await power.enable_battery_voltage_state_change_notify(self, is_enabled, target=1, timeout=timeout)

    async def on_battery_voltage_state_change_notify(self, handler=None, timeout=None):
        '''battery_voltage_state_change_notify

        :param coroutine handler: called asynchronously, takes form handler(state)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            power.on_battery_voltage_state_change_notify(self, target=1, handler=handler, timeout=timeout)
        )

    async def raw_motors(self, left_mode, left_speed, right_mode, right_speed, timeout=None):
        '''raw_motors

        :param uint8_t left_mode:  
        :param uint8_t left_speed:  
        :param uint8_t right_mode:  
        :param uint8_t right_speed:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await drive.raw_motors(self, left_mode, left_speed, right_mode, right_speed, target=2, timeout=timeout)

    async def reset_yaw(self, timeout=None):
        '''reset_yaw

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await drive.reset_yaw(self, target=2, timeout=timeout)

    async def drive_with_heading(self, speed, heading, flags, timeout=None):
        '''drive_with_heading

        :param uint8_t speed:  
        :param int16_t heading:  
        :param uint8_t flags: drive_flags 
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await drive.drive_with_heading(self, speed, heading, flags, target=2, timeout=timeout)

    async def set_sensor_streaming_mask(self, interval, packet_count, data_mask, timeout=None):
        '''set_sensor_streaming_mask

        :param uint16_t interval:  
        :param uint8_t packet_count:  
        :param uint32_t data_mask:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.set_sensor_streaming_mask(self, interval, packet_count, data_mask, target=2, timeout=timeout)

    async def get_sensor_streaming_mask(self, timeout=None):
        '''get_sensor_streaming_mask

        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: interval(uint16_t), packet_count(uint8_t), data_mask(uint32_t)
        '''
        return await sensor.get_sensor_streaming_mask(self, target=2, timeout=timeout)

    async def on_sensor_streaming_data_notify(self, handler=None, timeout=None):
        '''sensor_streaming_data_notify

        :param coroutine handler: called asynchronously, takes form handler(sensor_data)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            sensor.on_sensor_streaming_data_notify(self, target=1, handler=handler, timeout=timeout)
        )

    async def get_encoder_counts(self, timeout=None):
        '''get_encoder_counts

        :param float timeout: maximum time to await a response

        :returns: encoder_counts(int16_t array)
        '''
        return await sensor.get_encoder_counts(self, target=2, timeout=timeout)

    async def get_euler_angles(self, timeout=None):
        '''get_euler_angles

        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: pitch(float), roll(float), extended_roll(float), yaw(float)
        '''
        return await sensor.get_euler_angles(self, target=2, timeout=timeout)

    async def get_gyro_degrees_per_second(self, timeout=None):
        '''get_gyro_degrees_per_second

        :param float timeout: maximum time to await a response

        :rtype: tuple
        :returns: pitch(float), roll(float), yaw(float)
        '''
        return await sensor.get_gyro_degrees_per_second(self, target=2, timeout=timeout)

    async def set_extended_sensor_streaming_mask(self, data_mask, timeout=None):
        '''set_extended_sensor_streaming_mask

        :param uint32_t data_mask:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.set_extended_sensor_streaming_mask(self, data_mask, target=2, timeout=timeout)

    async def get_extended_sensor_streaming_mask(self, timeout=None):
        '''get_extended_sensor_streaming_mask

        :param float timeout: maximum time to await a response

        :returns: data_mask(uint32_t)
        '''
        return await sensor.get_extended_sensor_streaming_mask(self, target=2, timeout=timeout)

    async def enable_gyro_max_notify(self, is_enabled, timeout=None):
        '''enable_gyro_max_notify

        :param bool is_enabled:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.enable_gyro_max_notify(self, is_enabled, target=2, timeout=timeout)

    async def on_gyro_max_notify(self, handler=None, timeout=None):
        '''gyro_max_notify

        :param coroutine handler: called asynchronously, takes form handler(flags)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            sensor.on_gyro_max_notify(self, target=2, handler=handler, timeout=timeout)
        )

    async def configure_collision_detection(self, method, x_threshold, x_speed, y_threshold, y_speed, dead_time, timeout=None):
        '''configure_collision_detection

        :param uint8_t method:  
        :param uint8_t x_threshold:  
        :param uint8_t x_speed:  
        :param uint8_t y_threshold:  
        :param uint8_t y_speed:  
        :param uint8_t dead_time:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.configure_collision_detection(self, method, x_threshold, x_speed, y_threshold, y_speed, dead_time, target=2, timeout=timeout)

    async def on_collision_detected_notify(self, handler=None, timeout=None):
        '''collision_detected_notify

        :param coroutine handler: called asynchronously, takes form handler(acceleration_x, acceleration_y, acceleration_z, axis, power_x, power_y, speed, time)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            sensor.on_collision_detected_notify(self, target=2, handler=handler, timeout=timeout)
        )

    async def get_bot_to_bot_infrared_readings(self, timeout=None):
        '''get_bot_to_bot_infrared_readings

        :param float timeout: maximum time to await a response

        :returns: sensor_data(uint32_t)
        '''
        return await sensor.get_bot_to_bot_infrared_readings(self, target=2, timeout=timeout)

    async def start_robot_to_robot_infrared_broadcasting(self, far_code, near_code, timeout=None):
        '''start_robot_to_robot_infrared_broadcasting

        :param uint8_t far_code:  
        :param uint8_t near_code:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.start_robot_to_robot_infrared_broadcasting(self, far_code, near_code, target=2, timeout=timeout)

    async def stop_robot_to_robot_infrared_broadcasting(self, timeout=None):
        '''stop_robot_to_robot_infrared_broadcasting

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.stop_robot_to_robot_infrared_broadcasting(self, target=2, timeout=timeout)

    async def send_robot_to_robot_infrared_message(self, infrared_code, front_left_strength, front_right_strength, back_right_strength, back_left_strength, timeout=None):
        '''send_robot_to_robot_infrared_message

        :param uint8_t infrared_code:  
        :param uint8_t front_left_strength:  
        :param uint8_t front_right_strength:  
        :param uint8_t back_right_strength:  
        :param uint8_t back_left_strength:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.send_robot_to_robot_infrared_message(self, infrared_code, front_left_strength, front_right_strength, back_right_strength, back_left_strength, target=2, timeout=timeout)

    async def listen_for_robot_to_robot_infrared_message(self, infrared_code, listen_duration, timeout=None):
        '''listen_for_robot_to_robot_infrared_message

        :param uint8_t infrared_code:  
        :param uint32_t listen_duration:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.listen_for_robot_to_robot_infrared_message(self, infrared_code, listen_duration, target=2, timeout=timeout)

    async def on_robot_to_robot_infrared_message_received_notify(self, handler=None, timeout=None):
        '''robot_to_robot_infrared_message_received_notify

        :param coroutine handler: called asynchronously, takes form handler(infrared_code)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            sensor.on_robot_to_robot_infrared_message_received_notify(self, target=2, handler=handler, timeout=timeout)
        )

    async def get_ambient_light_sensor_value(self, timeout=None):
        '''get_ambient_light_sensor_value

        :param float timeout: maximum time to await a response

        :returns: ambient_light_white_channel_value(float)
        '''
        return await sensor.get_ambient_light_sensor_value(self, target=1, timeout=timeout)

    async def enable_color_detection_notification(self, enable, interval, minimum_confidence_threshold, timeout=None):
        '''enable_color_detection_notification

        :param bool enable:  
        :param uint16_t interval:  milliseconds
        :param uint8_t minimum_confidence_threshold:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.enable_color_detection_notification(self, enable, interval, minimum_confidence_threshold, target=1, timeout=timeout)

    async def on_color_detection_notify(self, handler=None, timeout=None):
        '''color_detection_notify

        :param coroutine handler: called asynchronously, takes form handler(red, green, blue, confidence, color_classification)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            sensor.on_color_detection_notify(self, target=1, handler=handler, timeout=timeout)
        )

    async def get_current_detected_color_reading(self, timeout=None):
        '''get_current_detected_color_reading

        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.get_current_detected_color_reading(self, target=1, timeout=timeout)

    async def enable_color_detection(self, enable, timeout=None):
        '''enable_color_detection

        :param bool enable:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await sensor.enable_color_detection(self, enable, target=1, timeout=timeout)

    async def set_bluetooth_device_name(self, name, target, timeout=None):
        '''set_bluetooth_device_name

        :param str name:  
        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await connection.set_bluetooth_device_name(self, name, target, timeout=timeout)

    async def get_bluetooth_device_name(self, target, timeout=None):
        '''get_bluetooth_device_name

        :param uint8_t target: 1 or 2
        :param float timeout: maximum time to await a response

        :returns: name(std::string)
        '''
        return await connection.get_bluetooth_device_name(self, target, timeout=timeout)

    async def set_all_leds_with_32_bit_mask(self, led_group, led_brightness_values, timeout=None):
        '''set_all_leds_with_32_bit_mask

        :param uint32_t led_group: led_groups 
        :param led_brightness_values: 
        :type led_brightness_values: array of uint8_ts (up to 32)
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await io.set_all_leds_with_32_bit_mask(self, led_group, led_brightness_values, target=1, timeout=timeout)

    async def enable_usb_status_async(self, enable, timeout=None):
        '''enable_usb_status_async

        :param bool enable:  
        :param float timeout: maximum time to await a response

        :returns: (None)
        '''
        return await io.enable_usb_status_async(self, enable, target=2, timeout=timeout)

    async def on_usb_connection_status_notify(self, handler=None, timeout=None):
        '''usb_connection_status_notify

        :param coroutine handler: called asynchronously, takes form handler(usb_connection_status)
        :param float timeout: maximum time to await a response

        :returns: Task (Future) from which `handler` will be called
        '''
        return asyncio.ensure_future(
            io.on_usb_connection_status_notify(self, target=2, handler=handler, timeout=timeout)
        )

    async def get_usb_connection_status(self, timeout=None):
        '''get_usb_connection_status

        :param float timeout: maximum time to await a response

        :returns: usb_connection_status(uint8_t)
        '''
        return await io.get_usb_connection_status(self, target=2, timeout=timeout)
