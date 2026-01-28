import numpy as np
import pandas as pd

from data.loader import load_prices
from model.garch import forecast_garch_vol
from model.realized_vol import realized_vol
from model.regime import classify_regime

SYMBOLS = [
    "EURUSD","GBPUSD","USDJPY","USDCHF","AUDUSD","NZDUSD","USDCAD",
    "EURGBP","GBPJPY","EURJPY","AUDJPY","CHFJPY",
    "XAUUSD","NQ"
]

results = []

for symbol in SYMBOLS:
    try:
        prices = load_prices(symbol)

        # safety check
        if len(prices) < 100:
            continue

        returns = np.diff(np.log(prices))

        rv = realized_vol(returns)
        fv = forecast_garch_vol(returns)

        vr, regime = classify_regime(fv, rv)

        results.append([
            symbol,
            round(fv * 100, 2),
            round(rv * 100, 2),
            round(vr, 2),
            regime
        ])

    except Exception:
        # skip symbols with bad or missing data (e.g. NQ on Stooq)
        continue

df = pd.DataFrame(
    results,
    columns=["Symbol", "Forecast Vol %", "Median Vol %", "VR", "Regime"]
)

print("\nDAILY VOLATILITY REGIME\n")
print(df.to_string(index=False))
