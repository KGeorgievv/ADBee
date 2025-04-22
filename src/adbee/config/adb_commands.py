# ADB commands for storage information
command_total_storage = "shell df -h /data | grep /data | awk '{print $2}'"
command_used_storage = "shell df -h /data | grep /data | awk '{print $3}'"
command_free_storage = "shell df -h /data | grep /data | awk '{print $4}'"

# ADB commands for memory information
command_total_memory = "shell cat /proc/meminfo | grep MemTotal | awk '{print $2}'"
command_free_memory = "shell cat /proc/meminfo | grep MemFree | awk '{print $2}'"
command_available_memory = "shell cat /proc/meminfo | grep MemAvailable | awk '{print $2}'"

# ADB commands for battery information
command_battery_info = "shell dumpsys battery"

# ADB commands for device information
command_device_name = "shell getprop ro.product.model"
command_device_serial_number = "get-serialno"
command_device_android_version = "shell getprop ro.build.version.release"
command_device_api_level = "shell getprop ro.build.version.sdk"
command_device_manufacturer = "shell getprop ro.product.manufacturer"

# ADB commands for network information
command_network_info = "shell dumpsys wifi"
command_ip_info = "shell ip addr show wlan0"

# ADB commands for CPU information
command_cpu_list = "shell ls /sys/devices/system/cpu/ | grep '^cpu[0-9]'"
command_cpu_active_cores = "shell cat /sys/devices/system/cpu/cpu*/online | grep -c 1"
command_process_activity = "shell top -n 1"

# ADB commands for CPU frequency information
def command_cpu_min_frequency(cpu_id):
    return f"shell cat /sys/devices/system/cpu/{cpu_id}/cpufreq/scaling_min_freq"

def command_cpu_max_frequency(cpu_id): 
    return f"shell cat /sys/devices/system/cpu/{cpu_id}/cpufreq/scaling_max_freq"

def command_cpu_current_frequency(cpu_id):
    return f"shell cat /sys/devices/system/cpu/{cpu_id}/cpufreq/scaling_cur_freq"
