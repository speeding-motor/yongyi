# coding=utf-8
# @Author : AYY

import pandas as pd
import numpy as np
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR
import matplotlib.pyplot as plt


def main():

    df = pd.read_csv('all_data_finance.csv', encoding="utf-8", error_bad_lines=True)
    df1 = pd.read_csv('all_data_buy_sale.csv', encoding="utf-8", error_bad_lines=True)
    df_finance = df[['股票代码', '交易日期', 'pos_time', 'stock_num', 'share_value', 'remain_cash', 'money']]
    df = df1.merge(df_finance, on=['股票代码', '交易日期'], how='left')

    df.loc[0, 'money'] = 100000
    df['money'].fillna(inplace=True, method='ffill')

    x1 = df['交易日期']
    y1 = df['收盘价']
    short_price_mean = df['short_price_mean']
    long_price_mean = df['long_price_mean']

    fig = plt.figure(figsize=(50, 50))
    fig.suptitle('share price')
    # First subplot
    ax = fig.add_subplot(2, 1, 1)
    ax.plot(x1, y1, x1, short_price_mean, x1, long_price_mean)
    ax.set_ylabel('share_price')

    ax = fig.add_subplot(2,1,2)
    ax.plot(x1, df['money'])
    ax.set_ylabel('money')
    plt.savefig('money.png')
    plt.show()


if __name__ == '__main__':
    main()


