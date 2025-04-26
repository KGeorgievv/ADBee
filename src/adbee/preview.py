from .adbee import ADBee

adbee = ADBee()
divider = "=" * 50

devices = adbee.get_devices()
for device in devices:
    # Get device information
    device_info = adbee.get_device_info(device=device)

    # Print device information
    print("Device Information ({device})".format(device=device))
    print(divider)

    for key, value in device_info.items():
        print(f"{key}: {value}")

    # Get storage usage
    storage_info = adbee.get_storage_info(device=device)
    
    # Print storage usage information
    print("\nStorage Information ({device})".format(device=device))
    print(divider)

    for key, value in storage_info.items():
        print(f"{key}: {value} GB")

    # Get memory usage
    memory_info = adbee.get_memory_info(device=device)

    # Print memory usage information
    print("\nMemory Information ({device})".format(device=device))
    print(divider)

    for key, value in memory_info.items():
        print(f"{key}: {value} MB")

    # Get battery information
    battery_info = adbee.get_battery_info(device=device)

    # Print battery information
    print("\nBattery Information ({device})".format(device=device))
    print(divider)

    for key, value in battery_info.items():
        if key == "battery_temp":
            print(f"{key}: {int(value) / 10} °C")
        else:
            print(f"{key}: {value}")

    # Get network information
    network_info = adbee.get_network_info(device=device)

    # Print network information
    print("\nNetwork Information ({device})".format(device=device))
    print(divider)
    for key, value in network_info.items():
        print(f"{key}: {value}")

    # Get CPU information
    cpu_info = adbee.get_cpu_info(device=device)

    # Print CPU information
    print("\nCPU Information ({device})".format(device=device))
    print(divider)

    for key, value in cpu_info.items():
        print(f"{key}: {value}")
