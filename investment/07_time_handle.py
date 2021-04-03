# coding=utf-8
# @Author : AYY

import pandas as pd

df = pd.read_csv('data/sh600000.csv', skiprows=1, nrows=5, encoding='gbk')

# str_time = '1999年1月11日'
# print(pd.to_datetime(str_time))

time = pd.to_datetime(df['交易日期'])
print(time, type(time[0]))

data_time = pd.todatetime(pd.DataFrame)

print('year', time.dt.year)
print('week', time.dt.week)
print('dayofyear', time.dt.dayofyear)

print('dayofweek', time.dt.dayofweek)
print('dayofweek', time.dt.weekday)
print('dayinmonth', time.dt.days_in_month)
print('month_end', time.dt.is_month_end)