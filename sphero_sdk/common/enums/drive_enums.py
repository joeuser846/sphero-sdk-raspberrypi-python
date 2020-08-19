#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x16-driving.json
# Device ID:          0x16
# Device Name:        drive
# Timestamp:          08/19/2020 @ 14:35:30.922554 (UTC)

from enum import IntEnum


__all__ = ['LinearVelocitySlewMethodsEnum',
           'ControlSystemTypesEnum',
           'ControlSystemIdsEnum',
           'RawMotorModesEnum',
           'MotorIndexesEnum',
           'DriveFlagsBitmask',
           'XyPositionDriveFlagsBitmask',
           'RcDriveFlagsBitmask']


class CommandsEnum(IntEnum): 
    raw_motors = 0x01
    reset_yaw = 0x06
    drive_with_heading = 0x07
    set_default_control_system_for_type = 0x0E
    set_custom_control_system_timeout = 0x22
    enable_motor_stall_notify = 0x25
    motor_stall_notify = 0x26
    enable_motor_fault_notify = 0x27
    motor_fault_notify = 0x28
    get_motor_fault_state = 0x29
    drive_tank_si_units = 0x32
    drive_tank_normalized = 0x33
    drive_rc_si_units = 0x34
    drive_rc_normalized = 0x35
    drive_with_yaw_si = 0x36
    drive_with_yaw_normalized = 0x37
    drive_to_position_si = 0x38
    drive_to_position_normalized = 0x39
    xy_position_drive_result_notify = 0x3A
    set_drive_target_slew_parameters = 0x3C
    get_drive_target_slew_parameters = 0x3D
    drive_stop_custom_decel = 0x3E
    active_controller_stopped_notify = 0x3F
    restore_default_drive_target_slew_parameters = 0x40
    get_stop_controller_state = 0x41
    drive_stop = 0x42
    restore_default_control_system_timeout = 0x43
    get_active_control_system_id = 0x44
    restore_initial_default_control_systems = 0x45
    get_default_control_system_for_type = 0x46


class LinearVelocitySlewMethodsEnum(IntEnum):
    constant = 0
    proportional = 1


class ControlSystemTypesEnum(IntEnum):
    control_system_type_stop = 0
    control_system_type_raw_motor = 1
    control_system_type_tank_drive = 2
    control_system_type_drive_with_yaw = 3
    control_system_type_rc_drive = 4
    control_system_type_xy_position_drive = 5
    control_system_type_infrared_drive = 6
    control_system_type_magnetometer_drive = 7


class ControlSystemIdsEnum(IntEnum):
    decelerating_stop = 0
    raw_motor = 1
    tank_drive = 2
    drive_with_yaw_advanced_mode = 3
    drive_with_yaw_basic_mode = 4
    rc_drive_rate_mode = 5
    rc_drive_slew_mode = 6
    xy_position_drive = 7
    infrared_follow_and_evade = 8
    magnetometer_calibration = 9


class RawMotorModesEnum(IntEnum):
    off = 0
    forward = 1
    reverse = 2


class MotorIndexesEnum(IntEnum):
    left_motor_index = 0
    right_motor_index = 1


class DriveFlagsBitmask(IntEnum):
    none = 0
    drive_reverse = 1
    boost = 2
    fast_turn = 4
    left_direction = 8
    right_direction = 16
    enable_drift = 32


class XyPositionDriveFlagsBitmask(IntEnum):
    none = 0
    force_reverse = 1
    auto_reverse = 2


class RcDriveFlagsBitmask(IntEnum):
    none = 0
    slew_linear_velocity = 1
