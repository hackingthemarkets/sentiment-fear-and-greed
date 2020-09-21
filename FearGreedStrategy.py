import backtrader as bt
import datetime 

class FearGreedStrategy(bt.Strategy):

    def __init__(self):
        self.fear_greed = self.datas[0].fear_greed
        self.close = self.datas[0].close

    def next(self):
        size = int(self.broker.getcash() / self.close[0])

        if self.fear_greed[0] < 10 and not self.position:
            self.buy(size=size)
        if self.fear_greed[0] > 94 and self.position.size > 0:
            self.sell(size=self.position.size)
