# coding=utf-8
# @Author : AYY

import pandas as pd
import numpy as np
from decimal import Decimal, ROUND_HALF_UP
import tools

"""
确定不能买卖的情况
1、当日涨停：不能买入
2、当日跌停：不能卖出
其他：股票停牌...休市
"""


def handle_data():
    df = pd.read_csv('all_data_strategy.csv', encoding='utf-8', nrows=1000, skip_blank_lines=True, error_bad_lines=True)
    df.drop(columns=["开盘价", "最高价", "最低价", "成交量", "成交额", "daily_rise_fall"],
            inplace=True)

    df['涨停价'] = df['前收盘价'] * 1.1
    df['跌停价'] = df['前收盘价'] * 0.9

    df['涨停价'] = df['涨停价'].apply(lambda x: float(Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
    df['跌停价'] = df['跌停价'].apply(lambda x: float(Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
    df['recovery_close_price'] = df['recovery_close_price'].apply(
        lambda x: float(Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
    df['short_price_mean'] = df['short_price_mean'].apply(
        lambda x: float(Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
    df['long_price_mean'] = df['long_price_mean'].apply(
        lambda x: float(Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))

    """因为采用的是尾盘操作，所以在购买当天，仓位=0，售出当天，仓位=1"""
    buy = df['buy'] & (df['收盘价'] < df['涨停价'])  # 发出购买信号 & 能买，不能买仓位保持和之前一致
    sale = df['sale'] & (df['收盘价'] > df['跌停价'])  # 发出卖出信号 & 能卖， 不能卖仓位保持和之前一致

    df.loc[buy, 'pos'] = 1  # 表示已购买持仓
    df.loc[sale, 'pos'] = 0  # 表示卖出
    df['pos'] = df['pos'].fillna(method='pad', inplace=False)  # 不能买仓位保持和之前一致,不能卖仓位保持和之前一致
    df['pos'] = df['pos'].shift(1)  # 尾盘交易，购买当天不算持仓

    """购买时的购买价格，每次购买成交价 = 上一日收盘价 + 0.1"""
    df['buy_price'] = df['收盘价'].apply(lambda x: float(Decimal(str(x + tools.SLIP_POINT)).quantize(Decimal('0.01'),
                                                                                                  rounding=ROUND_HALF_UP)))
    df['sale_price'] = df['收盘价'].apply(lambda x: float(Decimal(str(x - tools.SLIP_POINT)).quantize(Decimal('0.01'),
                                                                                                   rounding=ROUND_HALF_UP)))
    df['buy_price'] = df['buy_price'].shift(1)
    df['sale_price'] = df['sale_price'].shift(1)

    df.to_csv('all_data_buy_sale.csv', index=False)


if __name__ == "__main__":
    handle_data()
