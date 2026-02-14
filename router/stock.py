from fastapi import APIRouter, HTTPException
from services.stock_service import fetch_stock
from schema.stock import StockResponse

router = APIRouter(prefix="/stock",tags=["Stock"])

@router.get("/{symbol}",response_model=StockResponse)
def get_stock(symbol:str):
    data=fetch_stock(symbol)

    if not data:
        raise HTTPException(404,"Stock not Found!")
    
    return data;
