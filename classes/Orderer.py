from constants import INTERVALS
class Orderer:
    def __init__(self, account, market, messenger, exchangeClient):
        self.Account = account
        self.ExchangeClient = exchangeClient
        self.Market = market
        self.Messenger = messenger

    def getOpenOrderQuantity(self):
        currentPrice = self.Messenger.DataStore.liveOhlc.close
        leverage = self.Market.actualLeverage


        def getOpenCost(self):
            # TODO: make sure this is under the max for the leverage for this symbol
            
            marketAsset = self.Market.asset

            if(marketAsset == 'BUSD'):
                return leverage * self.Account.maxOpenBUSD
            if(marketAsset == 'USDT'):
                return leverage * self.Account.maxOpenUSDT

        openCost = getOpenCost(self)


        # TODO: Orderer should calculate stop loss and estimated liquidation
            #TODO: Based on est. liquidation, order size should be reduced until
            # est. liquidation is outside of calculated stop loss
        return 



        # TODO: calculate how much based on price, leverage, portfolio size

    def generateOrderPayload(self, side, positionSide):

