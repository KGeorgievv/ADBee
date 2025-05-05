from pydantic import BaseModel
from typing import List

class CpuFrequency(BaseModel):
    cpu_id: str
    min: int
    max: int
    cur: int

class CpuUsage(BaseModel):
    total: int
    user: int
    nice: int
    sys: int
    idle: int
    iow: int
    irq: int
    sirq: int
    host: int

class Cpu(BaseModel):
    cpu_count: int
    cpu_active_count: str
    cpu_usage: CpuUsage
    cpu_frequency: List[CpuFrequency]
