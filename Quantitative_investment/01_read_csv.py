# coding=utf-8

import pandas as pd
import numpy as np
import math
from io import StringIO

file_path = "data/sh600000.csv"


def read_data():
    # df = pd.read_csv(file_path, index_col=['交易日期'], skiprows=1, encoding='gbk')
    df = pd.read_csv(file_path, skiprows=1, encoding='gbk',
                     index_col=['交易日期'],  skip_blank_lines=True, nrows=10,
                    )
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_rows', 5)
    pd.set_option('precision', 1)

    print(df)
# #   查看整体数据
#     print(df.shape)
#     print(df.columns)
#     print(df.index)
#     print('*'*10)
#     print(df.dtypes,'\n', df.describe)
#     print(df.sample(frac=0.5))

#     读取部分列, 部分行
    p = df['股票名称']
    print(p, type(p))

    print(df.loc['1999-11-10'])



if __name__ == "__main__":
    read_data()
    # df = pd.read_csv('data/test.csv', index_col=[1, 0])
    # print(df, type(df))
