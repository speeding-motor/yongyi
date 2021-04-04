# coding=utf-8
# @Author : AYY

import pandas as pd

pd.set_option('display.expand_frame_repr', False)
df = pd.read_csv('data/sh600000.csv', encoding='gbk', skiprows=1, nrows=5, error_bad_lines=True)
df['price'] = [1,2,3,4,5]

df['收盘价_3'] = df['price'].rolling(3).mean()
df['收盘价_3'] = df['price'].rolling(3).max()

df['price_mean'] = df['price'].expanding.mean()
print(df)
