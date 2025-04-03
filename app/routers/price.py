from fastapi import APIRouter, HTTPException
from typing import Optional
from app.handlers.price import get_prices
from app.models.price import PriceResponse

router = APIRouter(
    prefix="/api/floki-prices",
    tags=["floki-prices"]
)

@router.get("/{time_range}", response_model=PriceResponse)
async def get_floki_prices(time_range: str, limit: Optional[int] = None):
    return await get_prices(time_range, limit)