from adbee.adbee import ADBee
import time
import asyncio

adbee = ADBee()
divider = "=" * 50

async def measure_execution_time(func, *args, **kwargs):
    """Measures the execution time of a function."""
    start_time = time.perf_counter()  # Record the start time
    
    result = await func(*args, **kwargs)  # Await the async function
    
    end_time = time.perf_counter()  # Record the end time
    execution_time = end_time - start_time  # Calculate the elapsed time
    print(divider)
    print(f"Execution Time of {func.__name__}: {execution_time:.4f} seconds")
    
    return result  # Return the result of the function

async def preview_device_info(device=None):
    device_info = await measure_execution_time(
        func=adbee.get_device_info,
        device=device
    )

    print("Device Information ({device})".format(device=device))
    print(divider)
    print(device_info)

async def preview_storage_info(device=None):
    storage_info = await measure_execution_time(
        func=adbee.get_storage_info,
        device=device
    )
    
    print("Storage Information ({device})".format(device=device))
    print(divider)
    print(storage_info)

async def preview_memory_info(device=None):
    memory_info = await measure_execution_time(
        func=adbee.get_memory_info,
        device=device
    )

    print("Memory Information ({device})".format(device=device))
    print(divider)
    print(memory_info)

async def preview_battery_info(device=None):
    battery_info = await measure_execution_time(
        func=adbee.get_battery_info,
        device=device
    )

    print("Battery Information ({device})".format(device=device))
    print(divider)
    print(battery_info)

async def preview_network_info(device=None):
    network_info = await measure_execution_time(
        func=adbee.get_network_info,
        device=device
    )

    print("Network Information ({device})".format(device=device))
    print(divider)
    print(network_info)

async def preview_cpu_info(device=None):
    cpu_info = await measure_execution_time(
        func=adbee.get_cpu_info,
        device=device
    )

    print("CPU Information ({device})".format(device=device))
    print(divider)
    print(cpu_info)


async def preview_data(device=None):
    devices = await adbee.get_devices()
    tasks = []
    
    for device in devices:
        tasks.append(asyncio.create_task(preview_device_info(device=device)))
        tasks.append(asyncio.create_task(preview_storage_info(device=device)))
        tasks.append(asyncio.create_task(preview_memory_info(device=device)))
        tasks.append(asyncio.create_task(preview_battery_info(device=device)))
        tasks.append(asyncio.create_task(preview_network_info(device=device)))
        tasks.append(asyncio.create_task(preview_cpu_info(device=device)))
    
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

async def main():
    await measure_execution_time(preview_data)

# Run the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
