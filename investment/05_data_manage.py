# coding=utf-8
# @Author : AYY

import pandas as pd
#
pd.set_option('display.expand_frame_repr', False)
df = pd.read_csv('data/sh600000.csv', encoding='gbk', skiprows=1, nrows=5, skip_blank_lines=True, error_bad_lines=True)
print(df)

# sort data
df.sort_values(axis=0, by=['股票名称', '交易日期',], inplace=True, ascending=True)
print(df)

# merge data   append  drop_duplicates
df1 = df.loc[1:4, '股票代码': '开盘价']
df2 = df.loc[:, '股票代码': '开盘价']
print(df1)
print(df2)

df3 = df1.append(df2)
print(df3)
df3['股票名称'] = [1,2,3,4,5,6,7,8]

df3.drop_duplicates(keep='first', subset=['交易日期','股票名称'], inplace=True, ignore_index=False)
print(df3)

df3.reset_index(inplace=True, drop=True)
print(df3)

df3.rename(columns={'股票代码':1,  '股票名称':2      ,  '交易日期':2  ,  '开盘价':4}, inplace=True)
print(df3)