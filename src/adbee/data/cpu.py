from utils.adb import execute
from config.adb_commands import (
    command_cpu_list,
    command_cpu_active_cores,
    command_process_activity,
    command_cpu_min_frequency,
    command_cpu_max_frequency,
    command_cpu_current_frequency
)
import re

def percent(part, cpu_total):
    return int(round((part / cpu_total) * 100)) if cpu_total else 0

def get_cpu_frequency(device=None):
    """
    Get CPU frequency information.
    :param device: Device ID
    :return: Dictionary with CPU frequency information
    """
    cpu_list = execute(command_cpu_list, device=device)
    cpu_frequencies = []

    for cpu in cpu_list.split():
        cpu_id = cpu.strip()
        min_freq = execute(command_cpu_min_frequency(cpu_id), device=device)
        max_freq = execute(command_cpu_max_frequency(cpu_id), device=device)
        cur_freq = execute(command_cpu_current_frequency(cpu_id), device=device)

        cpu_frequency = {
            "cpu_id": cpu_id,
            "min": int(min_freq) / 1000,
            "max": int(max_freq) / 1000,
            "cur": int(cur_freq) / 1000,
        }
        cpu_frequencies.append(cpu_frequency)
    
    return cpu_frequencies

def get_cpu_info(device=None):
    """
    Get CPU information.
    :param device: Device ID
    :return: Dictionary with CPU information
    """
    cpu_list = execute(command_cpu_list, device=device)
    cpu_active_cores_count = execute(command_cpu_active_cores, device=device)

    process_info = execute(command_process_activity, device=device)

    # Extract CPU info
    cpu_match = re.findall(r'(\d+)%(\w+)', process_info)
    cpu_stats = {key: int(value) for value, key in cpu_match}
    
    cpu_total = cpu_stats.get("cpu", 0)

    return {
        "cpu_count": len(cpu_list.split()),
        "cpu_active_count": cpu_active_cores_count,
        "cpu_usage": {
            "total": 100,
            "user": percent(cpu_stats.get("user", 0), cpu_total),
            "nice": percent(cpu_stats.get("nice", 0), cpu_total),
            "sys": percent(cpu_stats.get("sys", 0), cpu_total),
            "idle": percent(cpu_stats.get("idle", 0), cpu_total),
            "iow": percent(cpu_stats.get("iow", 0), cpu_total),
            "irq": percent(cpu_stats.get("irq", 0), cpu_total),
            "sirq": percent(cpu_stats.get("sirq", 0), cpu_total),
            "host": percent(cpu_stats.get("host", 0), cpu_total),
        },
        "cpu_frequency": get_cpu_frequency(device=device),
    }
