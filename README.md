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

```python
import adbee

adbee = adbee.ADBee()
devices = adbee.get_devices()

for device in devices:
  
    # Get device information
    device_info = adbee.get_device_info(device=device)

    # Print device information
    print("Device Information ({device})".format(device=device))
    print("=" * 50)

    for key, value in device_info.items():
        print(f"{key}: {value}")
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
