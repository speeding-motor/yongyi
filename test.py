# coding=utf-8
# @Author : AYY

import pandas as pd
import numpy as np
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR

df = pd.DataFrame({'a':[1,2], 'b':[2,3]})
print(df)


a = df['a'].iloc[-1]
print(a)

df['a'].iloc[-1] = df['a'].iloc[-1] + 100
print(df)