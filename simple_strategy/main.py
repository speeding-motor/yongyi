# coding=utf-8
# @Author : AYY

import buy_sale
import finance_evaluate
import strategy

'''
    简单的股票量化投资模型，主要功能有：

    1、确定策略（购买、售出信号）、确定最优参数：这里主要根据股价移动平均线来确定，购买、卖出信号
    2、购买、实际持仓
    3、计算资金复利曲线、查看最终结果

'''


def main():
    strategy.main()
    buy_sale.handle_data()
    finance_evaluate.evaluate_profit()


if __name__ == "__main__":
    main()
