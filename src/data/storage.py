from utils.adb import execute
from config.adb_commands import (
    command_total_storage,
    command_used_storage,
    command_free_storage,
)

def get_storage_info(device=None):

    def strip_g(value):
        return value.replace("G", "").strip()
    
    total_storage = execute(command_total_storage, device)
    used_storage = execute(command_used_storage, device)
    free_storage = execute(command_free_storage, device)

    return {
        "total_storage": strip_g(total_storage),
        "used_storage": strip_g(used_storage),
        "free_storage": strip_g(free_storage),
    }