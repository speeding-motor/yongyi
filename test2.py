# coding=utf-8
# @Author : AYY
import pandas as pd

c = "2020/10/4"
str = ["2021/10/4", "2000/10/4"]

dt = pd.to_datetime(str)
print(dt < c)


if __name__ == "__main__":
    pass
