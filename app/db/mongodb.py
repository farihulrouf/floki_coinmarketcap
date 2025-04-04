from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_mongo_client():
    MONGODB_URI = os.getenv("MONGODB_URI")
    return MongoClient(MONGODB_URI)

def get_floki_collection():
    client = get_mongo_client()
    db = client.crypto_data
    return db.floki_prices

def get_btc_collection():
    client = get_mongo_client()
    db = client.crypto_data
    return db.btc
