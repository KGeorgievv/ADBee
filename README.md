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
- ⚙️ **CPU Info**: Includes cpu utilization percentage, per core frequencies
- 🔁 Device filtering supported via `-s <device>` (ADB multiple device support)

## 🖥️ Prerequisites

- [Python 3.x](https://www.python.org/)
- ADB installed and accessible via terminal (`adb devices` should work)
- USB debugging enabled on the Android device
- Permissions granted for ADB debugging

## 📦 Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/KGeorgievv/ADBee.git
```

Or clone and install in development mode:

```bash
git clone https://github.com/KGeorgievv/ADBee.git
cd ADBee
pip install -e .
```

## 🧪 Example Usage

### Basic Usage
```python
from adbee import ADBee

# Initialize ADBee
adb = ADBee()

# Get list of connected devices
devices = adb.get_devices()
print(f"Connected devices: {devices}")

# Get basic device info
device_info = adb.get_device_info()
print(f"Device info: {device_info}")
```

### Comprehensive Device Information
```python
from adbee import ADBee

adb = ADBee()

# Specify a device (optional)
device = "DEVICE_SERIAL"  # or None for default device

# Get various device statistics
storage = adb.get_storage_info(device=device)
memory = adb.get_memory_info(device=device)
battery = adb.get_battery_info(device=device)
network = adb.get_network_info(device=device)
cpu = adb.get_cpu_info(device=device)

# Print collected information
print("Storage Info:", storage)
print("Memory Info:", memory)
print("Battery Info:", battery)
print("Network Info:", network)
print("CPU Info:", cpu)
```

### Working with Multiple Devices
```python
from adbee import ADBee

adb = ADBee()
devices = adb.get_devices()

for device in devices:
    print(f"\nCollecting info for device: {device}")
    
    # Collect all device information
    info = {
        "device": adb.get_device_info(device=device),
        "storage": adb.get_storage_info(device=device),
        "memory": adb.get_memory_info(device=device),
        "battery": adb.get_battery_info(device=device),
        "network": adb.get_network_info(device=device),
        "cpu": adb.get_cpu_info(device=device)
    }
    
    # Print formatted output
    for category, data in info.items():
        print(f"\n{category.upper()}:")
        for key, value in data.items():
            print(f"  {key}: {value}")
```

## 📂 ADBee Functions

| Function Name | Description |
|---------------|-------------|
| `get_devices()` | Returns list of connected adb devices |
| `get_device_info(device=None)` | Returns model, serial number, Android version, API level, and manufacturer |
| `get_memory_info(device=None)` | Returns total, free, and available memory (in MB) |
| `get_storage_info(device=None)` | Returns total, used, and free storage on `/data` (in GB) |
| `get_battery_info(device=None)` | Returns detailed battery information including health, level, and temperature |
| `get_network_info(device=None)` | Returns WiFi status, SSID, IP address, and MAC address |
| `get_cpu_info(device=None)` | Returns total cores, active cores, utilization percentage, frequiencies per core |

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
