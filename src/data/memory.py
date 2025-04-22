from utils.adb import execute
from config.adb_commands import (
    command_total_memory,
    command_free_memory,
    command_available_memory,
)
import math

def get_memory_info(device=None):
    total_memory = execute(command_total_memory, device)
    free_memory = execute(command_free_memory,  device)
    available_memory = execute(command_available_memory, device)

    return {
        "total_memory": math.ceil(int(total_memory) / 1024),
        "free_memory": math.ceil(int(free_memory) / 1024),
        "available_memory": math.ceil(int(available_memory) / 1024),
    }