from pydantic import BaseModel

class Memory(BaseModel):
    total_memory: int
    free_memory: int
    available_memory: int
