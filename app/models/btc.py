from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Btc(BaseModel):
    id: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float
    symbol: str
    interval: str
