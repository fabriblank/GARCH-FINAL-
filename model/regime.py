def classify_regime(forecast_vol, realized_vol):
    vr = forecast_vol / realized_vol
    if vr >= 1.25:
        return vr, "TRADE DAY"
    elif vr >= 1.0:
        return vr, "NEUTRAL"
    else:
        return vr, "NO TRADE"
