from pydantic import BaseModel

class Battery(BaseModel):
    ac_powered: bool
    usb_powered: bool
    wireless_powered: bool
    dock_powered: bool
    status: int
    health: int
    level: int
    voltage: int
    temperature: float
    technology: str
    capacity_level: int
    maximum_capacity: int
    design_capacity: int
