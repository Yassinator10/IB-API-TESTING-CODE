from socket import timeout
from symtable import Symbol
from ibapi.client import *
from ibapi.wrapper import *
import datetime
import time
from ibapi.tag_value import TagValue
from ibapi.contract import ComboLeg
import threading
datetime.datetime.now()
port = 7497


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        
        mycontract = Contract()
        #mycontract.conId = 14895034
        #mycontract.conId = 756733

        mycontract.symbol = "AAPL"
        mycontract.secType = "STK"
        mycontract.exchange = "ISLAND"
        #mycontract.primaryExchange = "ARCA"
        mycontract.currency = "USD"

        self.reqHistoricalData(
            reqId=orderId,
            contract=mycontract,
            endDateTime="20230501 23:59:59 UTC",
            durationStr= "1 D",
            barSizeSetting = "30 mins",
            whatToShow= "TRADES", 
			useRTH=0, 
			formatDate=1, 
			keepUpToDate=0,
			chartOptions=[]
        )

    def historicalData(self, reqId: int, bar: BarData):
        #if bar.open == bar.close:
        print(reqId, bar)


    def historicalDataEnd(self, reqId: int, start: str, end: str):
        print(reqId, start, end)
        self.disconnect()

    # def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
    #     print(reqId, errorCode, errorString, advancedOrderRejectJson)



app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()
