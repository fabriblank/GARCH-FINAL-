import pandas as pd
import requests
from io import StringIO

STOOQ_MAP = {
    "EURUSD": "EURUSD",
    "GBPUSD": "GBPUSD",
    "USDJPY": "USDJPY",
    "USDCHF": "USDCHF",
    "AUDUSD": "AUDUSD",
    "NZDUSD": "NZDUSD",
    "USDCAD": "USDCAD",
    "EURGBP": "EURGBP",
    "GBPJPY": "GBPJPY",
    "EURJPY": "EURJPY",
    "AUDJPY": "AUDJPY",
    "CHFJPY": "CHFJPY",
    "XAUUSD": "XAUUSD",
    "NQ": "NDQ"
}

def load_prices(symbol, years=5):
    url = f"https://stooq.com/q/d/l/?s={STOOQ_MAP[symbol]}&i=d"
    csv = requests.get(url).text
    df = pd.read_csv(StringIO(csv))

    # normalize headers
    df.columns = [c.lower() for c in df.columns]

    # possible close column names on stooq
    for col in ["close", "adj close", "zamkniecie"]:
        if col in df.columns:
            prices = df[col].astype(float).values
            return prices[-years * 252:]

    raise ValueError(f"No close price column found for {symbol}")
