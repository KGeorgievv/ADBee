from pydantic import BaseModel

class Network(BaseModel):
    wifi_status: str
    wifi_ssid: str
    ip_address: str
    mac_address: str
