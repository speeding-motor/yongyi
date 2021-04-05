# coding=utf-8
# @Author : AYY

import pandas as pd
import numpy as np
from decimal import Decimal, ROUND_HALF_UP

"""
确定不能买卖的情况
1、当日涨停：不能买入
2、当日跌停：不能卖出
其他：股票停牌...休市
"""


def read_data():
    df = pd.read_csv('all_data.csv', encoding='utf-8', nrows=1000, skip_blank_lines=True, error_bad_lines=True)
    df.drop(columns=["开盘价", "最高价", "最低价", "成交量", "成交额", "daily_rise_fall", "recovery_factor"],
            inplace=True)

    df['涨停价'] = df['前收盘价'] * 1.1
    df['跌停价'] = df['前收盘价'] * 0.9

    df['涨停价'] = df['涨停价'].apply(lambda x: float(Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
    df['跌停价'] = df['跌停价'].apply(lambda x: float(Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
    df['recovery_close_price'] = df['recovery_close_price'] .apply(lambda x: float(Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
    df['short_price_mean'] = df['short_price_mean'] .apply(lambda x: float(Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
    df['long_price_mean'] = df['long_price_mean'] .apply(lambda x: float(Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))

    enable_buy = df['收盘价'] < df['涨停价']  # 能购买
    enable_sale = df['收盘价'] > df['跌停价']  # 能卖出


    # 发出买的信号，且能购买
    buy = df['buy'] & enable_buy
    sale = df['sale'] & enable_sale

    df['en_buy'] = enable_buy
    df['en_sale'] = enable_sale
    df.loc[buy, 'pos'] = 1  # 表示已购买持仓
    df.loc[sale, 'pos'] = 0  # 表示卖出

    df.to_csv('test.csv', index=False)






if __name__ == "__main__":
    read_data()
