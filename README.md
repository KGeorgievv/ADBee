<p align="center">
  <img src="images/icon.png" alt="Android Device Info Logo" width="150"/>
</p>

# ADBee

A lightweight Python utility to fetch **Android device information** via ADB (Android Debug Bridge). This tool retrieves detailed data such as storage, memory, battery status, device metadata, and network configuration using simple terminal commands.

## 🔧 Features

- 📦 **Storage Usage**: View total, used, and free storage on `/data`
- 🧠 **Memory Stats**: Get total, free, and available memory in MB
- 🔋 **Battery Info**: Includes status, health, temperature, and charging state
- 📱 **Device Metadata**: Model, manufacturer, Android version, API level
- 🌐 **Network Info**: WiFi status, SSID, IP address, and MAC address
- 🔁 Device filtering supported via `-s <device>` (ADB multiple device support)

## 🖥️ Prerequisites

- [Python 3.x](https://www.python.org/)
- ADB installed and accessible via terminal (`adb devices` should work)
- USB debugging enabled on the Android device
- Permissions granted for ADB debugging

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/KGeorgievv/ADBee.git
cd adbee
```

## 🧪 Example Usage

```python
from device_info import (
    get_device_info,
    get_memory_usage,
    get_storage_usage,
    get_battery_info,
    get_device_network_info
)

# Without specifying a device (for single device connected)
print(get_device_info())
print(get_memory_usage())
print(get_storage_usage())
print(get_battery_info())
print(get_device_network_info())

# With device serial number
device_id = "emulator-5554"
print(get_device_info(device=device_id))
```

## 📂 Module Functions

| Function Name | Description |
|---------------|-------------|
| `get_device_info(device=None)` | Returns model, serial number, Android version, API level, and manufacturer |
| `get_memory_usage(device=None)` | Returns total, free, and available memory (in MB) |
| `get_storage_usage(device=None)` | Returns total, used, and free storage on `/data` (in GB) |
| `get_battery_info(device=None)` | Returns detailed battery information including health, level, and temperature |
| `get_device_network_info(device=None)` | Returns WiFi status, SSID, IP address, and MAC address |

## 📸 Sample Output

```json
{
  "name": "Pixel 5",
  "serial_number": "ABC123XYZ456",
  "android_version": "13",
  "api_level": "33",
  "manufacturer": "Google"
}
```

## 🛠️ Debugging Tip

If you're seeing errors like `Error: device not found`, make sure:
- Your device is connected and recognized by `adb devices`
- USB debugging is enabled and permission is granted

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Contributing

Feel free to submit issues or pull requests! Suggestions to support additional ADB diagnostics or enhance parsing logic are welcome.
