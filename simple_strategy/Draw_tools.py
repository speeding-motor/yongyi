# coding=utf-8
# @Author : AYY

import matplotlib.pylab as plt
import numpy as np
import pandas as pd
import tools

"""
绘制利润与购买点
1、短期平均价格线
2、长期平均价格线
3、购买时间点 ～ 卖出时间节点
4、总资金变化
"""

pd.set_option('display.expand_frame_repr', False)


def read_data():
    #
    df = pd.read_csv('../all_data_finance.csv', encoding="utf-8", error_bad_lines=True)
    df1 = pd.read_csv('../all_data_buy_sale.csv', encoding="utf-8", error_bad_lines=True)
    df_finance = df[['股票代码', '交易日期', 'pos_time', 'stock_num', 'share_value', 'remain_cash', 'money']]
    df = df1.merge(df_finance, on=['股票代码', '交易日期'], how='left')

    df.loc[0, 'money'] = tools.INITIAL_FINANCE
    df['money'].fillna(inplace=True, method='ffill')

    x1 = df['交易日期']
    y1 = df['收盘价']

    fig, ax = plt.subplots(2, 1, True)

    short_price_mean = df['short_price_mean']
    long_price_mean = df['long_price_mean']

    ax[0].plot(x1, y1, x1, short_price_mean, x1, long_price_mean)
    ax[1].plot(x1, df['money'])

    plt.show()

    df.to_csv('data.csv', index=False)
    return df



def main():
    """
    读取文件数据，绘制图形

    """
    fig, ax = plt.subplots(2, 1, True)  # Create a figure containing a single axes.
    ax[0].plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
    plt.show()


if __name__ == "__main__":
    read_data()
    # main()
