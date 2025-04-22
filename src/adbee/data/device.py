from utils.adb import execute
from config.adb_commands import (
    command_device_name,
    command_device_serial_number,
    command_device_android_version,
    command_device_api_level,
    command_device_manufacturer,
)

def get_device_info(device=None):
    return {
        "name": execute(command_device_name, device),
        "serial_number": execute(command_device_serial_number, device),
        "android_version": execute(command_device_android_version, device),
        "api_level": execute(command_device_api_level, device),
        "manufacturer": execute(command_device_manufacturer, device),
    }