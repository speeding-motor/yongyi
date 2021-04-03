# coding=utf-8
# @Author : AYY

import numpy as np
import pandas as pd

# pd.set_option('display.expand_frame_repr', False)
# df = pd.read_csv('data/sh600000.csv', nrows=5, skiprows=1, skip_blank_lines=True, error_bad_lines=True, encoding='gbk')
# print(df)

# df.drop(labels=2, inplace=True, axis=0)
# print(df)
# print('*'*10, '\n')
#
# ser = df.dropna(axis=0, how='any', inplace=False)
# print(ser)


a = np.arange(25, dtype=float).reshape((5, 5))
print(len(a))
for i in range(len(a)):
    a[i, :i] = np.nan
a[3, 0] = 25.0
df = pd.DataFrame(data=a, columns=list('ABCDE'))
print(df)

df.fillna(method='bfill', inplace=True)
print(df)

na = df.notnull()
print(na)