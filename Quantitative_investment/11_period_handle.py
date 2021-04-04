# coding=utf-8
# @Author : AYY

import pandas as pd

pd.set_option('display.expand_frame_repr', False)


def main():
    df = pd.read_csv('data/sh600000.csv', skiprows=1, encoding='gbk', nrows=100, skip_blank_lines=True, error_bad_lines=True)
    # df = df.loc[:, '股票代码':'开盘价']
    print(df)
    df['交易日期'] = pd.to_datetime(df['交易日期'])
    # sam = df.resample(rule='W', on='交易日期').last()
    #
    # print(type(sam))
    # print(sam)
    # 股票代码,股票名称,交易日期,开盘价,最高价,最低价,收盘价,前收盘价,成交量,成交额
    p_df = df.resample(rule='20D', on='交易日期', label='left').agg({'开盘价': ['max', 'mean'], '最高价': 'mean', '最低价': 'mean',
                                                               '成交量': 'sum'})

    print(p_df)


if __name__ == "__main__":
    main()
