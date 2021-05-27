class PositionMessageManager:


    # sample message
        # {
        # "id":3,
        # "result":[
        #     {
        #     "req":"gN0SiRrevtS4O0ufdCpzd4N0MzHu2lVmwbHh6hj4g9eTT9Yfe55eUc4klmsEhnwC@position",
        #     "res":{
        #         "positions":[
        #         {
        #             "entryPrice":"12044.90000003",
        #             "marginType":"ISOLATED", // margin type, "CROSSED" or "ISOLATED"
        #             "isAutoAddMargin":false,
        #             "isolatedMargin":"0.00006388", // isolated margin balance
        #             "leverage":125, // current leverage
        #             "liquidationPrice":"12002.39091452",  // estimated liquidation price
        #             "markPrice":"12046.06021667",  // current mark price
        #             "maxQty":"50",       // maximum quantity of base asset
        #             "positionAmt":"1",  // position amount
        #             "symbol":"BTCUSD_200925",   // symbol
        #             "unRealizedProfit":"0.00000079",  // unrealized PnL
        #             "positionSide":"LONG"       // position side
        #         },
        #         {
        #             "entryPrice":"0.0",
        #             "marginType":"ISOLATED",
        #             "isAutoAddMargin":false,
        #             "isolatedMargin":"0",
        #             "leverage":125,
        #             "liquidationPrice":"0",
        #             "markPrice":"12046.06021667",
        #             "maxQty":"50",
        #             "positionAmt":"0",
        #             "symbol":"BTCUSD_200925",
        #             "unRealizedProfit":"0.00000000",
        #             "positionSide":"SHORT"
        #         }
        #         ]
        #     }
        #     }
        # ]
        # }


    def onMessage(self, message):

    def onCloseMessage(self, message):
        self.DataStore.storeCloseMessage(message)
        closeSignal = self.Indicator.getCloseSignal(self.DataStore.data)
        
        self.Trader.handleCloseSignal(closeSignal)
    
    def onNonCloseMessage(self, message):
        openSignal = self.Indicator.getOpenSignal(self.DataStore.getDataForLiveIndicator(message))
        self.Trader.handleOpenSignal(openSignal)



    

