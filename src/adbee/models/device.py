from pydantic import BaseModel

class Device(BaseModel):
    name: str
    serial_number: str
    android_version: str
    api_level: str
    manufacturer: str
