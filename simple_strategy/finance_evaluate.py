# coding=utf-8
# @Author : AYY

import pandas as pd
import numpy as np
import tools
from decimal import Decimal,ROUND_FLOOR


'''
    计算投入后的具体收益：
    1、假设投入10w、交易手续费万2、印花税千1
    2、滑点：每次购买取卖一价，每次卖出选买一价
    3、计算实际持仓
    4、计算每次交易手续费、印花税
    5、根据持仓、涨跌幅、交易时间计算实际盈利
'''
pd.set_option('display.expand_frame_repr', False)


def evaluate_profit():
    """
    根据持仓计算资金涨跌幅
    1、确定买入时间点()、每次买入时，记录持仓时间 pos_time
    """
    global initial_finance
    df = pd.read_csv('all_data_buy_sale.csv', encoding='utf-8', error_bad_lines=True)
    pos_condiction = df['pos'] == 1.0
    pos_condiction_shift1 = df['pos'].shift(1).apply(lambda x: not x)

    #   当日持仓为1，且前日持仓为0，证明当日产生来购买行为，将buy_time 设置为 当日日期
    selected = (pos_condiction & pos_condiction_shift1).tolist()
    df.loc[selected, 'pos_time'] = df['交易日期']

    df['pos_time'] = df['pos_time'].fillna(method='ffill')
    df.loc[df['pos'] == 0, 'pos_time'] = pd.NA

    money = tools.INITIAL_FINANCE
    df_money_data = pd.DataFrame()

    for name, group in df.groupby(by='pos_time'):
        # print(name, '\n', group, '\n')

        money = __evaluate_profit_for_one_transaction(group, money)  # 计算每一次交易

        df_money_data = df_money_data.append(group, ignore_index=True)

    df_money_data['money'] = df_money_data['money'].apply(lambda x: Decimal(str(x)).quantize(Decimal('1'), ROUND_FLOOR))
    df_money_data['stock_num'] = df_money_data['stock_num'].apply(lambda x: Decimal(str(x)).quantize(Decimal('1'), ROUND_FLOOR))
    df_money_data['share_value'] = df_money_data['share_value'].apply(lambda x: Decimal(str(x)).quantize(Decimal('1'), ROUND_FLOOR))
    df_money_data['remain_cash'] = df_money_data['remain_cash'].apply(lambda x: Decimal(str(x)).quantize(Decimal('1'), ROUND_FLOOR))

    df_money_data.to_csv('all_data_finance.csv', index=False)


def __evaluate_profit_for_one_transaction(group, money):
    """
        计算每一笔操作的盈亏情况，包含了交易费用、印花税,第一次购买股票，使用初始资金，之后购买的金额，包含每次交易后的盈利和亏损
        1、剩余现金 ：根据当前可用金额，计算可购买的股票数量， 及剩余现金
        2、股票价值 ：计算持股期间股价涨幅变化，到交易结束时的盈亏情况
        3、每一轮buy & sale, 都将使用新的本金，重新计算1，2，3，最后得出最终盈亏金额

        T + 1 ->尾盘操作:
                思考：除权导致，昨天收盘价 ！= 前日收盘价， 如10送1
                    这时使用前收盘价，会导致剩余现金不等于真正实际情况， 故需要错位使用收盘价
    """
    pos_price = group.iloc[0, 14]

    # 只能一手一手的购买，一手是100股
    # 买入：交易手续费计算， stock_num * pos_price， 先计算全部资金购买股票，能购买多少股，在计算购买股票花了多少钱，根据购买股票价值*费率=手续费
    # 卖出印花税计算：
    stock_num = float(Decimal(str(money * (1-tools.TRANSACTION_FEE_RATE) / pos_price / 100)).quantize(Decimal('1'),
                                                                                                      rounding=ROUND_FLOOR)) * 100
    # 买入
    share_value = stock_num * pos_price
    transaction_cost = share_value * tools.TRANSACTION_FEE_RATE
    remain_cash = money - share_value - transaction_cost

    print("transaction_cost=:%s, remain_cash =%s" % (transaction_cost, remain_cash))

    # 卖出，可能会产生除权操作，股票数增多，股票价值涨跌幅度 = 收盘价复权价格的涨跌幅度
    # share_value = 最新股票市值 - 印花税
    recovery_factor = group['recovery_factor'].apply(lambda x: float(x))
    share_value = (recovery_factor / recovery_factor.iloc[0] * share_value)

    money = share_value + remain_cash

    group['stock_num'] = stock_num
    group['share_value'] = share_value
    group['remain_cash'] = remain_cash
    group['money'] = money

    # 最后卖出时，需要根据
    tax_cost = group['share_value'].iloc[-1] * tools.TAX_RATE  # 印花税
    group['money'].iloc[-1] = group['money'].iloc[-1] - tax_cost

    return money.iloc[-1]


if __name__ == "__main__":
    evaluate_profit()
