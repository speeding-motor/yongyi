# coding=utf-8
# @Author : AYY

import pandas as pd
import numpy as np
import tools


'''
    计算投入后的具体收益：
    1、假设投入10w、交易手续费万2、印花税千1
    2、滑点：每次购买取卖一价，每次卖出选买一价
    3、计算实际持仓
    4、计算每次交易手续费、印花税
    5、根据持仓、涨跌幅、交易时间计算实际盈利
'''
pd.set_option('display.expand_frame_repr', False)

initial_finance = tools.INITIAL_FINANCE
slip_point = tools.SLIP_POINT
tax = tools.TAX
transaction_fee = tools.TRANSACTION_FEE


def evaluate_profit():
    """
    根据持仓计算资金涨跌幅
    1、确定买入时间点()、每次买入时，记录buy_time
    """
    global initial_finance
    df = pd.read_csv('all_data_buy_sale.csv', encoding='utf-8', error_bad_lines=True)
    pos_condiction = df['pos'] == 1.0
    pos_condiction_shift1 = df['pos'].shift(1).apply(lambda x: not x)

    #   当日持仓为1，且前日持仓为0，证明当日产生来购买行为，将buy_time 设置为 当日日期
    selected = (pos_condiction & pos_condiction_shift1).tolist()
    df.loc[selected, 'buy_time'] = df['交易日期']

    df['buy_time'] = df['buy_time'].fillna(method='ffill')
    df.loc[df['pos'] == 0, 'buy_time'] = pd.NA

    global initial_finance, transaction_fee
    for name, group in df.groupby(by='buy_time'):
        # print(name, '\n', group, '\n')

        __evaluate_profit_for_one_transaction(group, initial_finance)  # 计算每一次交易

    df.to_csv('all_data_finance.csv', index=False)


def __evaluate_profit_for_one_transaction(group, cash):
    """
        计算每一笔操作的盈亏情况，包含了交易费用、印花税,第一次购买股票，使用初始资金，之后购买的金额，包含每次交易后的盈利和亏损
        1、剩余现金 ：根据当前可用金额，计算可购买的股票数量， 及剩余现金
        2、股票价值 ：计算持股期间股价涨幅变化，到交易结束时的盈亏情况
        3、每一轮buy & sale, 都将使用新的本金，重新计算1，2，3，最后得出最终盈亏金额

        T + 1 ->尾盘操作:
                思考：除权导致，昨天收盘价 ！= 前日收盘价， 如10送1
                    这时使用前收盘价，会导致剩余现金不等于真正实际情况， 故需要错位使用收盘价
    """

    print(group.iloc[0:1])
    exit()


if __name__ == "__main__":
    evaluate_profit()
