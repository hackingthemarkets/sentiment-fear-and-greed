import backtrader as bt
from FearGreedStrategy import FearGreedStrategy
from PutCallStrategy import PutCallStrategy
from VIXStrategy import VIXStrategy

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

class SPYPutCallFearGreedVixData(bt.feeds.GenericCSVData):
    lines = ('put_call', 'fear_greed', 'vix')

    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('adj', 5),
        ('volume', 6),
        ('put_call', 7),
        ('fear_greed', 8),
        ('vix', 9)
    )


class PutCallData(bt.feeds.GenericCSVData):

    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('put_call', 4),
        ('volume', -1),
        ('openinterest', -1)
    )


class FearGreedData(bt.feeds.GenericCSVData):

    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('fear_greed', 4),
        ('volume', -1),
        ('openinterest', -1)
    )


class VIXData(bt.feeds.GenericCSVData):

    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('vix', 4),
        ('volume', -1),
        ('openinterest', -1)
    )

spy_combined_csv_file = "datasets/spy-put-call-fear-greed-vix.csv"
put_csv_file = "datasets/put-call.csv"
vix_csv_file = "datasets/vix.csv"
fear_greed_csv_file = "datasets/fear-greed.csv"

spyCombinedFeed = SPYPutCallFearGreedVixData(dataname=spy_combined_csv_file)
putCallFeed = PutCallData(dataname=put_csv_file)
fearGreedFeed = FearGreedData(dataname=fear_greed_csv_file)
vixFeed = VIXData(dataname=vix_csv_file)

cerebro.adddata(spyCombinedFeed)
cerebro.adddata(putCallFeed)
cerebro.adddata(fearGreedFeed)
cerebro.adddata(vixFeed)

cerebro.addstrategy(FearGreedStrategy)
#cerebro.addstrategy(PutCallStrategy)
#cerebro.addstrategy(VIXStrategy)

cerebro.run()
cerebro.plot(volume=False)
