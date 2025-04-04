import json
from websocket import create_connection
from pymongo import MongoClient
from datetime import datetime

# 1. Koneksi ke MongoDB
mongo_client = MongoClient("mongodb://141.11.25.96:27017/")  # Ganti jika pakai cloud
db = mongo_client["crypto_data"]  # Nama database
collection = db["pepe_1m"]  # Nama collection

# 2. WebSocket Binance (1m candlestick)
ws_url = "wss://stream.binance.com:9443/ws/pepeusdt@kline_1m"  # 🔴 Ganti pair ke 'pepeusdt'

def save_to_mongodb(candle):
    # Struktur data untuk MongoDB
    candle_data = {
        "timestamp": datetime.fromtimestamp(candle['t'] / 1000),  # Convert ms to datetime
        "open": float(candle['o']),
        "high": float(candle['h']),
        "low": float(candle['l']),
        "close": float(candle['c']),
        "volume": float(candle['v']),
        "symbol": "PEPEUSDT",  # Diubah symbol
        "interval": "1m"
    }
    # Insert ke MongoDB (upsert untuk update jika data sudah ada)
    collection.update_one(
        {"timestamp": candle_data["timestamp"]},
        {"$set": candle_data},
        upsert=True
    )
    print("✅ Data saved:", candle_data["timestamp"], candle_data["close"])

# 3. Terima data real-time
ws = create_connection(ws_url)
while True:
    message = ws.recv()
    data = json.loads(message)
    candle = data['k']
    if candle['x']:  # Hanya simpan jika candle sudah ditutup (closed candle)
        save_to_mongodb(candle)