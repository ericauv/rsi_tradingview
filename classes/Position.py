class Position:
    def __init__(self, market):
        self.entryPrice = 0
        self.leverage = 1
        self.liquidationPrice = 0
        self.marginBalance = 0
        self.marginType = ''
        self.Market = market
        self.side = ''
        self.size = 0
        self.unrealizedProfit = 0

    def onMessage(self, message):
        self.entryPrice = message.entryPrice
        self.leverage = message.leverage
        self.liquidationPrice = self.liquidationPrice
        self.marginBalance = self.isolatedMargin
        self.marginType = message.marginType
        self.side = self.positionSide
        self.size = message.positionAmt
        self.unrealizedProfit = self.unRealizedProfit
