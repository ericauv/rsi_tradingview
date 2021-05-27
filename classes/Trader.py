from constants import SIGNALS 
from datetime import datetime

class Trader:
    ORDER_BUFFER_SECONDS = 5

    def __init__(self, messenger, market, exchangeClient):
        self.Messenger = messenger
        self.Market = market

        self.positionLong = {}
        self.positionShort = {}

        self.isInLongPosition = False
        self.isInShortPosition = False

        self.placedCloseLongPositionOrderTimestamp = 0
        self.placedCloseShortPositionOrderTimestamp = 0

        self.placedOpenLongPositionOrderTimestamp = 0
        self.placedOpenShortPositionOrderTimestamp = 0

        self.Exchange = exchangeClient

    def getHasRecentlyPlacedThisOrder(self, side, positionSide):
        def getIsPreviousOrderAssumedExpired(previousOrderTimestamp):
            return datetime.now().timestamp() - previousOrderTimestamp >= 5

        def getHasRecentlyPlacedOpenLongOrder(self):
            return getIsPreviousOrderAssumedExpired(self.placedOpenLongPositionOrderTimestamp) == False

        def getHasRecentlyPlacedOpenShortOrder(self):
            return getIsPreviousOrderAssumedExpired(self.placedOpenShortPositionOrderTimestamp) == False

        def getHasRecentlyPlacedCloseLongOrder(self):
            return getIsPreviousOrderAssumedExpired(self.placedCloseLongPositionOrderTimestamp) == False

        def getHasRecentlyPlacedCloseShortOrder(self):
            return getIsPreviousOrderAssumedExpired(self.placedCloseShortPositionOrderTimestamp) == False

        if(side == 'BUY'):
            if(positionSide == 'SHORT'):
                return getHasRecentlyPlacedOpenShortOrder()
            if(positionSide == 'LONG'):
                return getHasRecentlyPlacedOpenLongOrder()
        if(side == 'SELL'):
            if(positionSide == 'SHORT'):
                return getHasRecentlyPlacedCloseShortOrder()
            if(positionSide == 'LONG'):
                return getHasRecentlyPlacedCloseLongOrder()

    def handleOpenSignal(self, openSignal):
        if(openSignal == SIGNALS.OPEN.LONG):
            if(self.isInLongPosition == False and self.getHasRecentlyPlacedThisOrder('BUY', 'LONG') == False):
                return self.openLong()
            pass
        if(openSignal == SIGNALS.OPEN.SHORT):
            if(self.isInShortPosition == False and self.getHasRecentlyPlacedThisOrder('BUY', 'SHORT') == False):
                return self.openShort()
            pass
        pass

    def handleCloseSignal(self, closeSignal):
        if(closeSignal == SIGNALS.CLOSE.LONG):
            if(self.isInLongPosition == True and self.getHasRecentlyPlacedThisOrder('SELL', 'LONG') == False):
                self.closeLong()
            pass
        if(closeSignal == SIGNALS.CLOSE.SHORT and self.getHasRecentlyPlacedThisOrder('SELL', 'SHORT') == False):
            if(self.isInShortPosition):
                self.closeShort()
            pass
        pass

    def openLong(self):
        self.placedOpenLongPositionOrderTimestamp = datetime.now().timestamp()
        orderResponse = self.handleOrder('BUY', 'LONG')
        # TODO: Place open long order, store how much, store entry, etc. to set stop loss and take profits

    def openShort(self):
        self.placedOpenShortPositionOrderTimestamp = datetime.now().timestamp()
        # TODO: Place open short order, store how much, store entry, etc. to set stop loss and take profits

    def handleOrder(self, side, positionSide):
        self.Market.printMarketInfo()
        print(f'TRADER handling order:\n\tside: {side}\n\tpositionSide: {positionSide}')
