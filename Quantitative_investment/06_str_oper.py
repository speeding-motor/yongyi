# coding=utf-8
# @Author : AYY

import pandas as pd

pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv('data/sh600000.csv', encoding='gbk', skiprows=1, nrows=10)
print(df)
name = df['股票代码']
print(name)

print(name.str[0:2])
print(name.str.upper())
print(name.str.lower())
print(name.str.len())
print(name.str.strip())
print(name.str.contains('sh'))
print(name.str.replace('sh', 'shz'))