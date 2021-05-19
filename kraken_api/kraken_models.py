import numpy as np
from kraken_api.kraken import KrakenAPI
from helpers.datetime import current_milli_time
from datetime import datetime

class TickerResponse:
    def __init__(self, a, b, c, v, p, t, l, h, o, symbol):
        self.ask = a
        self.bid = b
        self.lastTrade = c
        self.volume = v
        self.volumeWeightedAverage = p
        self.numberOfTradesToday = t
        self.lowToday = l
        self.highToday = h 
        self.todaysOpen = o
        self.milliTime = current_milli_time()
        self.dateTime = datetime.now().strftime("%m/%d/%y %H:%M:%S")
        self.symbol = symbol
        self.organism_input = [float(a),float(b),float(c),float(v),float(p),float(t),float(l),float(h),float(o)]
        return
    def __str__(self):
        return "+++Ticker Response+++\n    Symbol("+self.symbol+") as of: "+self.dateTime+"\n    Ask: "+self.ask+"\n    Bid: "+self.bid+"\n    Last Trade: "+self.lastTrade+"\n    Volume: "+self.volume+"\n    Volume Weighted Avg: "+self.volumeWeightedAverage+"\n    Number of Trades Today: "+str(self.numberOfTradesToday)+"\n    Low Today: "+self.lowToday+"\n    High Today: "+self.highToday+"\n    Todays Open: "+self.todaysOpen + "\n++++END  RESPONSE++++"