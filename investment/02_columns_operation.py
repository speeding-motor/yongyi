# coding=utf-8
# @Author : AYY

import pandas as pd

pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv('data/sh600000.csv', encoding='gbk', nrows=5, skiprows=1)

print(df)

# 列加减、统计数据
df['mean'] = df['成交额'] / df['成交量']
df['mm'] = pd.DataFrame(pd.Series([1,2,pd.NA,2,4]))
print(df)

mean = df['成交额'].mean()
max = df['成交额'].max()
min = df['成交额'].min()
print(mean, max, min)

shift = df[['mm', 'mean']].shift(1, axis='columns',fill_value=None)
diff = df['mean'].diff(-1)
print(shift)
print(diff)

df.drop(['mean'], axis=1, inplace=True)
# df.drop([3], axis=0, inplace=True)
print(df)

pct = df[['mm']].pct_change(1)
print(pct)

sum = df['mm'].cumsum()
cumprod = df['mm'].cumprod()
print(sum)
print(cumprod)

rank = df[['mm']].rank(ascending=False, method='min', na_option='bottom', pct=True)
print(rank)

value_content = df['mm'].value_counts()
print(value_content)

