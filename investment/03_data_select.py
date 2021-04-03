# coding=utf-8
# @Author : AYY

import pandas as pd
'''
1、df[df['columns']=='']]
2、df.loc[:,:]

'''


pd.set_option('display.expand_frame_repr', False)
df = pd.read_csv('data/sh600000.csv', encoding='gbk', skiprows=1, nrows=5)

print(df)
names = df['股票名称']
print(names)

s1 = df[[True, True, True, False, False]]
print(s1)

s2 = df.loc[0:1, '股票代码':'交易日期']
print(s2)


