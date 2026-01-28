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
    df = df.tail(years * 252)
    df["Close"] = df["Close"].astype(float)
    return df["Close"].values
