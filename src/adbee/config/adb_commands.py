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
command_cpu_frequency_per_core = '''
grep "^cpu[0-9]" /proc/stat;
for cpu in /sys/devices/system/cpu/cpu[0-9]*; do
    name=$(basename $cpu);
    echo "$name:cur=$(cat $cpu/cpufreq/scaling_cur_freq 2>/dev/null) min=$(cat $cpu/cpufreq/scaling_min_freq 2>/dev/null) max=$(cat $cpu/cpufreq/scaling_max_freq 2>/dev/null)";
done;
echo END
'''
