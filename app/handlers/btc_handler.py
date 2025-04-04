from app.database import get_btc_collection
from bson import ObjectId
from datetime import datetime

def serialize_candle(doc):
    return {
        "id": str(doc["_id"]),
        "timestamp": doc["timestamp"].isoformat() if isinstance(doc["timestamp"], datetime) else doc["timestamp"],
        "open": doc["open"],
        "high": doc["high"],
        "low": doc["low"],
        "close": doc["close"],
        "volume": doc["volume"],
        "symbol": doc["symbol"],
        "interval": doc["interval"]
    }

def get_all_btc_candles(symbol: str = None):
    collection = get_btc_collection()
    query = {"symbol": symbol} if symbol else {}
    candles = collection.find(query).sort("timestamp", 1)
    return [serialize_candle(doc) for doc in candles]
