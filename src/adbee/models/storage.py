from pydantic import BaseModel

class Storage(BaseModel):
    total_storage: str
    used_storage: str
    free_storage: str
