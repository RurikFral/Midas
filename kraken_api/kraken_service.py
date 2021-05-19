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
        return
    def __str__(self):
        return "+++Ticker Response+++\n    Symbol("+self.symbol+") as of: "+self.dateTime+"\n    Ask: "+self.ask+"\n    Bid: "+self.bid+"\n    Last Trade: "+self.lastTrade+"\n    Volume: "+self.volume+"\n    Volume Weighted Avg: "+self.volumeWeightedAverage+"\n    Number of Trades Today: "+str(self.numberOfTradesToday)+"\n    Low Today: "+self.lowToday+"\n    High Today: "+self.highToday+"\n    Todays Open: "+self.todaysOpen + "\n++++END  RESPONSE++++"

class KrakenService():
    def __init__(self, symbol=None):
        #instansiate the api connection
        self.api = KrakenAPI()
        #if no symbol is given then set it to DOGE :D
        if symbol is None:
            symbol = "DOGEUSD"
            self.symbol = symbol
        return
    
    def getTicker(self):
        response = self.api.query_public("Ticker?pair="+self.symbol)
        return TickerResponse(response["result"]["XDGUSD"]["a"][0],response["result"]["XDGUSD"]["b"][0],response["result"]["XDGUSD"]["c"][0],response["result"]["XDGUSD"]["v"][0],response["result"]["XDGUSD"]["p"][0],response["result"]["XDGUSD"]["t"][0],response["result"]["XDGUSD"]["l"][0],response["result"]["XDGUSD"]["h"][0],response["result"]["XDGUSD"]["o"], self.symbol)

