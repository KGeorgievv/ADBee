from adbee.models import Device
from ..utils.adb import execute
from ..config.adb_commands import (
    command_device_name,
    command_device_serial_number,
    command_device_android_version,
    command_device_api_level,
    command_device_manufacturer,
)
import asyncio

async def get_device_info(device=None):
    name = await asyncio.to_thread(execute, command_device_name, device)
    serial_number = await asyncio.to_thread(execute, command_device_serial_number, device)
    android_version = await asyncio.to_thread(execute, command_device_android_version, device)
    api_level = await asyncio.to_thread(execute, command_device_api_level, device)
    manufacturer = await asyncio.to_thread(execute, command_device_manufacturer, device)

    result = Device(
        name=name,
        serial_number=serial_number,
        android_version=android_version,
        api_level=api_level,
        manufacturer=manufacturer,
    )

    return result.model_dump_json(indent=2)
