from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class PriceData(BaseModel):
    price: float
    currencies: str
    timestamp: datetime
    market_cap: str
    volume_24h: str
    fdv: str
    vol_mkt_cap_ratio: float
    total_supply: str
    max_supply: str
    circulating_supply: str
    percent_change_1h: float
    status_1h: str
    percent_change_24h: float
    status_24h: str

    class Config:
        json_encoders = {
            datetime: lambda v: {"$date": v.isoformat() + "Z"}  # Format MongoDB
        }

class PriceResponse(BaseModel):
    time_range: str
    count: int
    data: List[PriceData]