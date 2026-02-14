import yfinance as yf


def fetch_stock(symbol: str):
    try:
        stock=yf.Ticker(symbol)
        info=stock.info

        if "regularMarketPrice" not in info :
            return None
        
        return {
            "symbol": symbol.upper(),
            "price": info.get("regularMarketPrice"),
            "open": info.get("regularMarketOpen"),
            "high":info.get("dayHigh"),
            "low":info.get("dayLow"),
            "previous_close":info.get("previousClose"),
            "marketCap":info.get("marketCap"),
            "currency":info.get("currency"),
        }
    except Exception:
        return None