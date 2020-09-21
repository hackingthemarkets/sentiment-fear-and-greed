import backtrader as bt
import datetime 

class VIXStrategy(bt.Strategy):

    def __init__(self):
        self.vix = self.datas[0].vix
        self.close = self.datas[0].close

    def next(self):
        size = int(self.broker.getcash() / self.close[0])

        if self.vix[0] > 35 and not self.position:
            self.buy(size=size)
        if self.vix[0] < 10 and self.position.size > 0:
            self.sell(size=self.position.size)
