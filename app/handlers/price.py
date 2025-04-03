from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException
from app.db.mongodb import get_floki_collection
from app.models.price import PriceResponse, PriceData

def calculate_time_range(time_range: str) -> datetime:
    now = datetime.utcnow()
    
    time_mapping = {
        "15m": timedelta(minutes=15),
        "30m": timedelta(minutes=30),
        "1h": timedelta(hours=1),
        "24h": timedelta(hours=24),
        "7d": timedelta(days=7),
        "1m": timedelta(days=30),
        "3m": timedelta(days=90),
        "6m": timedelta(days=180),
        "9m": timedelta(days=270),
        "12m": timedelta(days=365),
    }
    
    if time_range not in time_mapping:
        raise ValueError("Invalid time range specified")
        
    return now - time_mapping[time_range]

async def get_prices(time_range: str, limit: Optional[int] = None) -> PriceResponse:
    try:
        start_time = calculate_time_range(time_range)
        collection = get_floki_collection()
        
        query = {"timestamp": {"$gte": start_time}}
        
        # Hapus projection untuk mendapatkan semua field
        cursor = collection.find(query).sort("timestamp", -1)
        
        if limit:
            cursor = cursor.limit(limit)
            
        results = [PriceData(**doc) for doc in cursor]
        
        if not results:
            raise HTTPException(status_code=404, detail="No data found")
            
        return PriceResponse(
            time_range=time_range,
            count=len(results),
            data=results
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))