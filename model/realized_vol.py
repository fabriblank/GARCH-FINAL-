import numpy as np

def realized_vol(returns, window=20):
    return np.median(np.abs(returns[-window:]))
