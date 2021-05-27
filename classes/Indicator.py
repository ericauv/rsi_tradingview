from stoch_rsi import stoch_rsi_tradingview
from constants import SIGNALS

class Indicator:

    # How far apart the liveD and liveK need to be to create an open signal
    liveDeltaForOpen = 5

    def __init__(self, messenger, stochRsiPeriod = 14, smoothK = 3, smoothD = 3):
        self.Messenger = messenger
        
        self.lastCloseD = 0
        self.lastCloseK = 0
        self.liveD = 0
        self.liveK = 0

        self.stochRsiPeriod = stochRsiPeriod
        self.smoothD = smoothD
        self.smoothK = smoothD
        self.dataPointsNeededForLiveCalculation = stochRsiPeriod + smoothK + smoothD

        self.openSignal = ''
        self.closeSignal = ''

    def calculateLastClose(self, data):
        k, d = self.calculate(data)
        
        self.lastCloseK = k
        self.lastCloseD = d
        
        return k, d

    def calculate(self, data):
        _rsi, k, d  = stoch_rsi_tradingview(data, self.stochRsiPeriod, self.smoothK, self.smoothD)
        
        self.liveD = d
        self.liveK = k

        return k, d

    def getCloseSignal(self, data):
        self.calculateLastClose(data)

        # TODO: Check that both k and d are numbers / defined

        if(self.lastCloseK < self.lastCloseD):
            self.closeSignal = SIGNALS.CLOSE.SHORT
        if(self.lastCloseK < self.lastCloseD):
            self.closeSignal = SIGNALS.CLOSE.LONG

        return self.closeSignal

    def getOpenSignal(self, data):
        self.calculate(data)
        
        # TODO: Check that both k and d are numbers / defined

        if(self.closeSignal == SIGNALS.CLOSE.SHORT and abs(self.liveD - self.liveK) >= self.liveDeltaForOpen):
            self.openSignal = SIGNALS.OPEN.LONG
        if(self.closeSignal == SIGNALS.CLOSE.LONG and abs(self.liveD - self.liveK) >= self.liveDeltaForOpen):
            self.openSignal = SIGNALS.OPEN.SHORT

        return self.openSignal
