# coding=utf-8
# @Author : AYY

import pandas as pd
import numpy as np

if __name__ == "__main__":
    rng = pd.date_range("1/1/2012", periods=20, freq="min")
    ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
    print(rng)
    print(ts)

    sampled = ts.resample('5t', label='right').sum()
    print(sampled)