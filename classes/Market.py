from constants import INTERVALS
class Market:
    def __init__(self, symbol, interval, contractType):
        def getAssetFromSymbol(self, symbol):
            if('USDT' in symbol):
                return 'USDT'
            if('BUSD' in symbol):
                return 'BUSD'

        def getRecommendedLeverage(interval):
            if(interval == INTERVALS.MINUTE_1):
                return 50
            if(interval == INTERVALS.MINUTE_5):
                return 30
            if(interval == INTERVALS.MINUTE_15):
                return 25
            if(interval == INTERVALS.HOUR_1):
                return 10

            return 10

        self.recommendedLeverage = getRecommendedLeverage(interval)
        self.actualLeverage = self.recommendedLeverage
        self.asset = getAssetFromSymbol(self, symbol)
        self.contractType = contractType
        self.interval = interval
        self.symbol = symbol

    def printMarketInfo(self):
        print(f'MARKET INFO:\n\tsymbol: {self.symbol}\n\tinterval: {self.interval}\n\tcontractType: {self.contractType}, recommendedLeverage: {self.recommendedLeverage}\n')

    def updateActualLeverage(self, message):
        # TODO: Subscribe to leverage update events, update actual leverage based on events
