from classes import Indicator, DataStore, Trader

class Messenger:
    def __init__(self, account, market, exchangeClient):
        self.Account = account
        self.Market = market
        self.DataStore = DataStore(self)
        self.Indicator = Indicator(self)
        self.Trader = Trader(self, market)
        self.ExchangeClient = exchangeClient
    
    def getIsCloseMessage(self, message):
        return message.k.x == True

    def onMessage(self, message):
        self.DataStore.updateLiveOhlc(message)

        if(self.getIsCloseMessage(message)):
            self.onCloseMessage(message)
        else:
            self.onNonCloseMessage(message)

    def onCloseMessage(self, message):
        self.DataStore.storeClose()
        closeSignal = self.Indicator.getCloseSignal(self.DataStore.data)
        
        self.Trader.handleCloseSignal(closeSignal)
    
    def onNonCloseMessage(self, message):
        openSignal = self.Indicator.getOpenSignal(self.DataStore.getDataForLiveIndicator(message))
        self.Trader.handleOpenSignal(openSignal)



    

