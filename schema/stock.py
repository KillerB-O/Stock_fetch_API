from pydantic import BaseModel
from typing import Optional

class StockResponse(BaseModel):
    symbol: str
    price: float
    open:Optional[float] = None
    high:Optional[float] = None
    low:Optional[float] = None
    previous_close: Optional[float] = None
    marketCap: Optional[int] = None
    currency: Optional[str] = None

