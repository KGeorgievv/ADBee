from utils.adb import execute
from config.adb_commands import (
    command_battery_info
)

status_map = {
    1: "Unknown",
    2: "Charging",
    3: "Discharging",
    4: "Not charging",
    5: "Full"
}

health_map = {
    1: "Unknown",
    2: "Good",
    3: "Overheat",
    4: "Dead",
    5: "Over voltage", 
    6: "Unspecified failure", 
    7: "Cold"
}

charging_state_map = {
    0: "Unknown",
    1: "Enabled",
    2: "Disabled",
    3: "Limited"
}

capacity_level_map = {
    0: "Unknown",
    1: "Critical",
    2: "Low",
    3: "Normal",
    4: "High",
    5: "Full"
}

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
    "charging_state",
    "capacity_level"
}
    
def get_battery_info(device=None):
    output = execute(command_battery_info, device)

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

        # Convert enums and temperature
        if key == "status":
            value = status_map.get(value, value)
        elif key == "health":
            value = health_map.get(value, value)
        elif key == "charging_state":
            value = charging_state_map.get(value, value)
        elif key == "capacity_level":
            value = capacity_level_map.get(value, value)
        elif key == "temperature":
            value = round(value / 10.0, 1)

        battery_info[key] = value

    return battery_info