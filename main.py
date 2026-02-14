from fastapi import FastAPI
from router import stock

app=FastAPI(title="Stock Fetch API")

app.include_router(stock.router)

@app.get("/")
def home():
    return {
        "message": "Stock API Running"
    }