# coding=utf-8
# @Author : AYY

import pandas as pd
import numpy as np


def main():
    df = pd.read_csv('data/sh600000.csv', skiprows=1, skip_blank_lines=True, error_bad_lines=True, encoding='gbk',
                     nrows=10)
    print(df)

    # agg
    # for name, group in df.groupby('股票代码'):
    #     print(name, '\n',  group)
    # df1 = df.groupby('股票代码').agg({'开盘价': 'mean', '最高价':'max'})
    # print(df1)

    # transform
    # df2 = df.groupby(['股票代码', '股票名称'])['成交量'].transform('mean')
    # print(df2)
    for name, group in df.groupby(['股票代码', '股票名称']):
        print(name, '\n',  group)


if __name__ == "__main__":
    main()
