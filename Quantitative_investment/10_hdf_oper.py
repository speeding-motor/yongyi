# coding=utf-8
# @Author : AYY

import pandas as pd


def to_hdf():
    df = pd.read_csv('data/sh600000.csv', skiprows=1, encoding='gbk')
    print(df)
    df.to_hdf('/data/hdf1.h5', key='key', encoding='gbk')


if __name__ == "__main__":
    to_hdf()