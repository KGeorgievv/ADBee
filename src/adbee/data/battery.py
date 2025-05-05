from adbee.models import Battery
from ..utils.adb import execute
from ..config.adb_commands import (
    command_battery_info
)
import asyncio

fields_to_extract = {
    "ac_powered",
    "usb_powered",
    "wireless_powered",
    "dock_powered",
    "status",
    "health",
    "level",
    "voltage",
    "temperature",
    "technology",
    "capacity_level",
    "maximum_capacity",
    "design_capacity",
}

async def get_battery_info(device=None):
    output = await asyncio.to_thread(execute, command_battery_info, device)

    battery_info = {}

    for line in output.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue

        key, value = map(str.strip, line.split(":", 1))
        key = key.lower().replace(" ", "_")

        if key not in fields_to_extract:
            continue

        # Handle types
        try:
            value = int(value)
        except ValueError:
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False

        battery_info[key] = value

    result = Battery(
        ac_powered=battery_info.get("ac_powered", False),
        usb_powered=battery_info.get("usb_powered", False),
        wireless_powered=battery_info.get("wireless_powered", False),
        dock_powered=battery_info.get("dock_powered", False),
        status=battery_info.get("status", 0),
        health=battery_info.get("health", 0),
        level=battery_info.get("level", 0),
        voltage=battery_info.get("voltage", 0),
        temperature=battery_info.get("temperature", 0),
        technology=battery_info.get("technology", "Unknown"),
        capacity_level=battery_info.get("capacity_level", 0),
        maximum_capacity=battery_info.get("maximum_capacity", 0),
        design_capacity=battery_info.get("design_capacity", 0),
    )

    return result.model_dump_json(indent=2)
