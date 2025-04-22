from ..utils.adb import execute
from ..config.adb_commands import (
    command_network_info,
    command_ip_info
)

def get_network_info(device=None):
    # Run a single adb command and capture all necessary output
    wifi_info = execute(command_network_info, device=device)
    ip_info = execute(command_ip_info, device=device)

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
        'wifi_status': wifi_status,
        'wifi_ssid': wifi_ssid,
        'ip_address': ip_address,
        'mac_address': mac_address,
    }
