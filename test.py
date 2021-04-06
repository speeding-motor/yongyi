# coding=utf-8
# @Author : AYY

import pandas as pd
import numpy as np
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR


s = pd.Series([1,2,3,4,6])
print(s , "...")

print(s.iloc[-1])