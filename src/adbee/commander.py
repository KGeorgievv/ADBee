from abc import ABC, abstractmethod

class ADBCommander(ABC):

    @abstractmethod
    def execute(self, command):
        """
        Execute a command on the device.
        :param command: Command to execute
        :return: Command output
        """
        pass

    @abstractmethod
    def get_devices(self):
        """
        Get a list of connected devices.
        :return: List of device IDs
        """
        pass

    @abstractmethod
    def get_device_info(self, device):
        """
        Get device information.
        :param device: Device ID
        :return: Dictionary with device information
        """
        pass

    @abstractmethod
    def get_storage_info(self, device):
        """
        Get storage usage information.
        :param device: Device ID
        :return: Dictionary with storage usage information
        """
        pass

    @abstractmethod
    def get_memory_info(self, device):
        """
        Get memory usage information.
        :param device: Device ID
        :return: Dictionary with memory usage information
        """
        pass

    @abstractmethod
    def get_battery_info(self, device):
        """
        Get battery information.
        :param device: Device ID
        :return: Dictionary with battery information
        """
        pass

    @abstractmethod
    def get_network_info(self, device):
        """
        Get network information.
        :param device: Device ID
        :return: Dictionary with network information
        """
        pass

    @abstractmethod
    def get_cpu_info(self, device):
        """
        Get CPU information.
        :param device: Device ID
        :return: Dictionary with CPU information
        """
        pass
    