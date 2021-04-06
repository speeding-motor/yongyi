# coding=utf-8
# @Author : AYY

import pandas as pd
import numpy as np
import os
import io
from tools import DATA_DIR

"""
根据股价移动平均线来确定，购买、卖出信号:
    1、购买信号：短期股价平均值  >   长期股价平均值
    2、卖出信号：短期股价平均值  <   长期股价平均值

    短期时间参数[3, 5, 7 10]
    长期时间参数[20、50、80、120]

"""

short_time_quantum = 5
long_time_quantum = 30

pd.set_option('display.max_colwidth', 5000)
pd.set_option('display.expand_frame_repr', False)


def __read_data():
    # 读取数据
    df = pd.DataFrame()
    for root, dirs, files in os.walk(DATA_DIR):
        for file_name in files:
            file_path = DATA_DIR + "/" + file_name

            print('file_path='+file_path)

            temp = pd.read_csv(file_path, skiprows=1, encoding='gbk', skip_blank_lines=True, error_bad_lines=True)
            df = df.append(temp,  ignore_index=True)
    # print(df[0:3])
    return df


def __handle_data(data):
    """
    股票代码 股票名称 交易日期 开盘价 最高价 最低价 收盘价 前收盘价 成交量  成交额
    股票会有配股、分送操作，所以需要进行对价格进行复权操作,复权价=
    均价 = sum{复权价}/time_gap
    """
    df_all = pd.DataFrame()
    for name, group in data.groupby('股票代码'):
        group.sort_values(by='交易日期', axis=0, inplace=True, ascending=True, ignore_index=True)

        group['daily_rise_fall'] = (group['收盘价'] / group['前收盘价']) - 1
        group['recovery_factor'] = (group['daily_rise_fall']+1).cumprod()  # 复权因子,以最初的股价为基准，每天的日涨跌幅为依据，计算此后每天的涨跌复权

        group['recovery_close_price'] = group['recovery_factor'] * (group.iloc[0]['收盘价'] / group.iloc[0]['recovery_factor'])

        group['short_price_mean'] = group.rolling(short_time_quantum, min_periods=1)['收盘价'].mean()
        group['long_price_mean'] = group.rolling(long_time_quantum, min_periods=1)['收盘价'].mean()

        # 买入信号 short > long, buy =1, sale=-1,
        group.loc[group['short_price_mean'] > group['long_price_mean'], 'buy'] = True
        group.loc[group['short_price_mean'] < group['long_price_mean'], 'sale'] = True

        df_all = df_all.append(group)

    df_all.to_csv('all_data_strategy.csv', index=False)


if __name__ == "__main__":
    data = __read_data()
    __handle_data(data)
