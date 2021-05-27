class Account:
    def __init__(self):
        self.balanceUSDT = 0
        self.balanceBUSD = 0
        self.maxOpen = 0
        self.maxOpenBUSD = 0
        self.maxOpenUSDT = 0

    def onMessage(self, message):

        def updateBalances(self, balances):

            def updateBalance(self, balances, symbol):
                if(balances):
                    balance = [x for x in balances if x.a == symbol]
                    if(balance):
                        if(symbol == 'BUSD'):
                            self.balanceBUSD = balance.wb
                        if(symbol == 'USDT'):
                            self.balanceUSDT = balance.wb

            updateBalance(self, balances, 'USDT')
            updateBalance(self, balances, 'BUSD')
        
        def updateMaxOpens(self):
            self.maxOpen = (self.balanceBUSD + self.balanceUSDT ) / 5
            self.maxOpenBUSD = min(self.maxOpen, self.balanceBUSD)
            self.maxOpenUSDT = min(self.maxOpen, self.balanceUSDT)

        balances = message.a.B

        updateBalances(self, balances)    
        updateMaxOpens(self, balances, 'BUSD')


    
