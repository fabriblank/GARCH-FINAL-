from arch import arch_model

def forecast_garch_vol(returns):
    model = arch_model(
        returns * 100,
        vol="Garch",
        p=1,
        q=1,
        dist="normal"
    )
    res = model.fit(disp="off")
    forecast = res.forecast(horizon=1)
    return (forecast.variance.iloc[-1, 0] ** 0.5) / 100
