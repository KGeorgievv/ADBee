from adbee.models import Storage
from ..utils.adb import execute
from ..config.adb_commands import (
    command_total_storage,
    command_used_storage,
    command_free_storage,
)

import asyncio

async def get_storage_info(device=None):

    def strip_g(value):
        return value.replace("G", "").strip()
    
    total_storage = await asyncio.to_thread(execute, command_total_storage, device)
    used_storage = await asyncio.to_thread(execute, command_used_storage, device)
    free_storage = await asyncio.to_thread(execute, command_free_storage, device)

    result = Storage(
        total_storage=strip_g(total_storage),
        used_storage=strip_g(used_storage),
        free_storage=strip_g(free_storage),
    )

    return result.model_dump_json(indent=2)
