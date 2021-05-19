from kraken_api.kraken_models import TickerResponse
from kraken_api.kraken import KrakenAPI
from helpers.datetime import current_milli_time
from datetime import datetime

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