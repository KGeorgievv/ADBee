from ..utils.adb import (
    execute,
    execute_shell
)
from ..config.adb_commands import (
    command_cpu_list,
    command_cpu_active_cores,
    command_process_activity,
    command_cpu_frequency_per_core
)
import re

def percent(part, cpu_total):
    return int(round((part / cpu_total) * 100)) if cpu_total else 0

def get_cpu_frequency(device=None):
    """
    Get CPU frequency information efficiently.
    :param device: Device ID
    :return: List of dictionaries with CPU frequency information
    """
    output = execute_shell(command_cpu_frequency_per_core, device=device)
    cpu_frequencies = []

    lines = output.strip().splitlines()

    for line in lines:
        line = line.strip()
        if not line or ":" not in line:
            continue

        cpu_id, rest = line.split(":", 1)
        freq_info = dict(item.split("=") for item in rest.strip().split())

        cur = freq_info.get("cur")
        minf = freq_info.get("min")
        maxf = freq_info.get("max")

        cpu_frequency = {
            "cpu_id": cpu_id,
            "min": int(minf) / 1000 if minf and minf.isdigit() else None,
            "max": int(maxf) / 1000 if maxf and maxf.isdigit() else None,
            "cur": int(cur) / 1000 if cur and cur.isdigit() else None,
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
