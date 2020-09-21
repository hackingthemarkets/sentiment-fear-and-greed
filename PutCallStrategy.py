import backtrader as bt
import datetime 

class PutCallStrategy(bt.Strategy):

    def __init__(self):
        self.put_call = self.datas[0].put_call
        self.close = self.datas[0].close

    def next(self):
        size = int(self.broker.getcash() / self.close[0])

        if self.put_call[0] > 1 and not self.position:
            self.buy(size=size)
        if self.put_call[0] < 0.45 and self.position.size > 0:
            self.sell(size=self.position.size)
