from adbee.models import Memory
from ..utils.adb import execute
from ..config.adb_commands import (
    command_total_memory,
    command_free_memory,
    command_available_memory,
)

import asyncio

async def get_memory_info(device=None):
    total_memory = await asyncio.to_thread(execute, command_total_memory, device)
    free_memory = await asyncio.to_thread(execute, command_free_memory, device)
    available_memory = await asyncio.to_thread(execute, command_available_memory, device)

    result = Memory(
        total_memory=total_memory,
        free_memory=free_memory,
        available_memory=available_memory,
    )

    return result.model_dump_json(indent=2)
