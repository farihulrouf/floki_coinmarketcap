from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.price import router as price_router

app = FastAPI(title="FLOKI Price API", description="API untuk data harga FLOKI dalam IDR")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(price_router)

@app.get("/")
async def root():
    return {
        "message": "FLOKI Price API",
        "endpoints": {
            "get_prices": "/api/floki-prices/{time_range}",
            "available_time_ranges": ["15m", "30m", "1h", "24h", "7d", "1m", "3m", "6m", "9m", "12m"]
        }
    }