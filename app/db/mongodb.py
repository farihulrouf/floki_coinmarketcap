from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_mongo_client():
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://141.11.25.96:27017")
    return MongoClient(MONGODB_URI)

def get_floki_collection():
    client = get_mongo_client()
    db = client.crypto_data
    return db.floki_prices