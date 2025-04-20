from adbee import (
    run_adb_command,
    get_device_info,
    get_storage_usage,
    get_memory_usage,
    get_battery_info,
    get_device_network_info,
)

divider = "=" * 50

adb_devices = run_adb_command("devices")
if "device" in adb_devices.splitlines()[-1]:
    # prase devices serials
    devices = adb_devices.splitlines()[1:]
    devices = [device.split()[0] for device in devices if "device" in device]
    
    print("Found", len(devices), "devices")
    print(divider)
    for device in devices:
        print(device)

    for device in devices:
        print(divider)
        print()
        print()

        # Get device information
        device_info = get_device_info(device=device)

        # Print device information
        print("Device Information ({device})".format(device=device))
        print(divider)

        for key, value in device_info.items():
            print(f"{key}: {value}")

        # Get storage usage
        storage_info = get_storage_usage(device=device)
        
        # Print storage usage information
        print("\nStorage Information ({device})".format(device=device))
        print("=" * 30)

        for key, value in storage_info.items():
            print(f"{key}: {value} GB")

        # Get memory usage
        memory_info = get_memory_usage(device=device)

        # Print memory usage information
        for key, value in memory_info.items():
            print(f"{key}: {value} MB")

        # Get battery information
        battery_info = get_battery_info(device=device)

        # Print battery information
        print("\nBattery Information ({device})".format(device=device))
        print("=" * 30)

        for key, value in battery_info.items():
            if key == "battery_temp":
                print(f"{key}: {int(value) / 10} °C")
            else:
                print(f"{key}: {value}")

        # Get network information
        network_info = get_device_network_info(device=device)

        # Print network information
        print("\nNetwork Information ({device})".format(device=device))
        print("=" * 30)
        for key, value in network_info.items():
            print(f"{key}: {value}")
        
else:
    print("No ADB device connected. Please connect a device and try again.")
    exit(1)