from adbee.models import Cpu
from ..utils.adb import (
    execute,
    execute_shell,
)
from ..config.adb_commands import (
    command_cpu_list,
    command_cpu_active_cores,
    command_process_activity,
    command_cpu_frequency_per_core
)
import re
import asyncio

def percent(part, cpu_total):
    return int(round((part / cpu_total) * 100)) if cpu_total else 0

async def get_cpu_frequency(device=None):
    """
    Get CPU frequency information efficiently.
    :param device: Device ID
    :return: List of dictionaries with CPU frequency information
    """
    output = await asyncio.to_thread(execute_shell, command_cpu_frequency_per_core, device=device)
    cpu_frequencies = []

    lines = output.strip().splitlines()

    for line in lines:
        line = line.strip()
        if not line or ":" not in line:
            continue

        cpu_id, rest = line.split(":", 1)
        freq_info = dict(item.split("=") for item in rest.strip().split())

        cpu_frequency = {
            "cpu_id": cpu_id,
            "min": freq_info.get("min"),
            "max": freq_info.get("max"),
            "cur": freq_info.get("cur"),
        }
        cpu_frequencies.append(cpu_frequency)

    return cpu_frequencies

async def get_cpu_info(device=None):
    """
    Get CPU information.
    :param device: Device ID
    :return: Dictionary with CPU information
    """
    cpu_list = await asyncio.to_thread(execute, command_cpu_list, device=device)
    cpu_active_cores_count = await asyncio.to_thread(execute, command_cpu_active_cores, device=device)
    process_info = await asyncio.to_thread(execute, command_process_activity, device=device)
    cpu_frequency = await get_cpu_frequency(device=device)

    # Extract CPU info
    cpu_match = re.findall(r'(\d+)%(\w+)', process_info)
    cpu_stats = {key: int(value) for value, key in cpu_match}
    
    cpu_total = cpu_stats.get("cpu", 0)

    result = Cpu(
        cpu_count=len(cpu_list.split()),
        cpu_active_count=cpu_active_cores_count,
        cpu_usage={
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
        cpu_frequency=cpu_frequency,
    )

    return result.model_dump_json(indent=2)
