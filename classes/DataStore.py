class DataStore:
    def __init__(self, messenger):
        self.Messenger = messenger
        self.ohlcData = []
        self.liveOhlc = {}

    def updateLiveOhlc(self, message):
        newOhlc = self.formatMessageToOhlc(message)
        self.liveOhlc = newOhlc
        return newOhlc

    def storeClose(self):
        self.data.append(self.liveOhlc)
    
    def formatMessageToOhlc(self, message):
        return {
            'open': message.k.o,
            'close': message.k.c,
            'high': message.k.h,
            'low': message.k.l
        }
    
    def getDataForLiveIndicator(self, Indicator):
        numberOfPointsToCopy = Indicator.dataPointsNeededForLiveCalculation
        
        liveDataSet = self.data[-numberOfPointsToCopy:].append(self.liveOhlc)

        return liveDataSet

