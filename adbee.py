import math
import subprocess

# Utility function to run ADB commands
def run_adb_command(command, device = None, use_shell=False):
    try:
        if device:
            command = f"-s {device} {command}"

        result = subprocess.check_output(["adb"] + command.split(), stderr=subprocess.STDOUT, shell=use_shell)
        return result.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"

# Function to get storage usage in GB
def get_storage_usage(device=None):

    def strip_g(value):
        return value.replace("G", "").strip()
    
    total_storage = run_adb_command("shell df -h /data | grep /data | awk '{print $2}'", device)
    used_storage = run_adb_command("shell df -h /data | grep /data | awk '{print $3}'", device)
    free_storage = run_adb_command("shell df -h /data | grep /data | awk '{print $4}'", device)

    return {
        "total_storage": strip_g(total_storage),
        "used_storage": strip_g(used_storage),
        "free_storage": strip_g(free_storage),
    }

# Function to get memory usage in MB
def get_memory_usage(device=None):
    total_memory = run_adb_command("shell cat /proc/meminfo | grep MemTotal | awk '{print $2}'", device)
    free_memory = run_adb_command("shell cat /proc/meminfo | grep MemFree | awk '{print $2}'",  device)
    available_memory = run_adb_command("shell cat /proc/meminfo | grep MemAvailable | awk '{print $2}'", device)

    return {
        "total_memory": math.ceil(int(total_memory) / 1024),
        "free_memory": math.ceil(int(free_memory) / 1024),
        "available_memory": math.ceil(int(available_memory) / 1024),
    }

def get_battery_info(device=None):
    output = run_adb_command("shell dumpsys battery", device)

    # Fields to keep
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

    # Enum mappings
    status_map = {
        1: "Unknown", 2: "Charging", 3: "Discharging", 4: "Not charging", 5: "Full"
    }

    health_map = {
        1: "Unknown", 2: "Good", 3: "Overheat", 4: "Dead", 5: "Over voltage", 6: "Unspecified failure", 7: "Cold"
    }

    charging_state_map = {
        0: "Unknown", 1: "Enabled", 2: "Disabled", 3: "Limited"
    }

    capacity_level_map = {
        0: "Unknown", 1: "Critical", 2: "Low", 3: "Normal", 4: "High", 5: "Full"
    }

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


# Fetch device details using ADB commands
def get_device_info(device=None):
    return {
        "name": run_adb_command("shell getprop ro.product.model", device),
        "serial_number": run_adb_command("get-serialno", device),
        "android_version": run_adb_command("shell getprop ro.build.version.release", device),
        "api_level": run_adb_command("shell getprop ro.build.version.sdk", device),
        "manufacturer": run_adb_command("shell getprop ro.product.manufacturer", device),
    }

def get_device_network_info(device=None):
    # Run a single adb command and capture all necessary output
    wifi_info = run_adb_command("shell dumpsys wifi", device=device)
    ip_info = run_adb_command("shell ip addr show wlan0", device=device)

    # Parse the wifi information
    wifi_status = None
    wifi_ssid = None
    for line in wifi_info.splitlines():
        line = line.strip()
        if "Wi-Fi is" in line:
            wifi_status = line.split()[2]  # Extracts the status
        elif "mWifiInfo SSID" in line:
            wifi_ssid = line.split('SSID: ')[1].split(',')[0].replace('"', '').strip()

    # Parse the ip address and mac address from ip_info
    ip_address = None
    mac_address = None

    for line in ip_info.splitlines():
        line = line.strip()
        if "inet " in line:
            ip_address = line.split()[1].split('/')[0]  # Extracts the IP address
        elif "link/ether" in line:
            mac_address = line.split()[1]  # Extracts the MAC address

    # Return the gathered information as a dictionary
    return {
        'wifi-status': wifi_status,
        'wifi-ssid': wifi_ssid,
        'ip-address': ip_address,
        'mac-address': mac_address,
    }
