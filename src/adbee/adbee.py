from .utils.adb import execute
from .commander import ADBCommander

from .data.device import get_device_info
from .data.storage import get_storage_info
from .data.battery import get_battery_info
from .data.memory import get_memory_info
from .data.network import get_network_info
from .data.cpu import get_cpu_info

import asyncio

class ADBee(ADBCommander):
    
    def execute(self, command, device=None):
        """
        Execute an ADB command synchronously.
        :param command: ADB command to execute
        :return: Command output
        """
        return execute(command, device)

    async def execute_async(self, command, device=None):
        """
        Execute an ADB command asynchronously using a separate thread.
        :param command: ADB command to execute
        :param device: Device to target
        :return: Command output
        """
        return await asyncio.to_thread(self.execute, command, device)

    async def get_devices(self):
        """
        Get a list of connected devices.
        :return: List of device serial numbers
        """
        adb_devices = await self.execute_async("devices")
        lines = adb_devices.strip().splitlines()

        if len(lines) <= 1:
            return []

        devices = []
        for line in lines[1:]:
            parts = line.split()
            if len(parts) == 2 and parts[1] == "device":
                devices.append(parts[0])

        return devices

    async def get_device_info(self, device):
        """
        Get device information.
        :param device: Device ID
        :return: Dictionary with device information
        """
        return await get_device_info(device)
    
    async def get_storage_info(self, device):
        """
        Get storage usage information.
        :param device: Device ID
        :return: Dictionary with storage usage information
        """
        return await get_storage_info(device)
    
    async def get_memory_info(self, device):
        """
        Get memory usage information.
        :param device: Device ID
        :return: Dictionary with memory usage information
        """
        return await get_memory_info(device)
    
    async def get_battery_info(self, device):
        """
        Get battery information.
        :param device: Device ID
        :return: Dictionary with battery information
        """
        return await get_battery_info(device)
    
    async def get_network_info(self, device):
        """
        Get network information.
        :param device: Device ID
        :return: Dictionary with network information
        """
        return await get_network_info(device)
    
    async def get_cpu_info(self, device):
        """
        Get CPU information.
        :param device: Device ID
        :return: Dictionary with CPU information
        """
        return await get_cpu_info(device)
    