from constants import SIGNALS 

def getCloseSignal(currentStochRsiD, currentStochRsiK):
    if(currentStochRsiK < currentStochRsiD):
            return SIGNALS.CLOSE.SHORT
    if(currentStochRsiK > currentStochRsiD):
            return SIGNALS.CLOSE.LONG
        
    pass

def getOpenSignal(liveStochRsiD, liveStochRsiK, currentStochRsiD, currentStochRsiK):
    if(getCloseSignal(currentStochRsiD, currentStochRsiK) == SIGNALS.CLOSE.SHORT and abs(liveStochRsiD - liveStochRsiK) >= 5):
        return SIGNALS.OPEN.LONG
    if(getCloseSignal(currentStochRsiD, currentStochRsiK) == SIGNALS.CLOSE.LONG and abs(liveStochRsiD - liveStochRsiK) >= 5):
        return SIGNALS.OPEN.SHORT

    pass

def handleOpenSignal(openSignal, isInLongPosition, isInShortPosition, handleOpenLong, handleOpenShort):
    if(openSignal == SIGNALS.OPEN.LONG):
        if(isInLongPosition == False):
            return handleOpenLong()
        pass
    if(openSignal == SIGNALS.OPEN.SHORT):
        if(isInShortPosition == False):
            return handleOpenShort()
        pass
    pass

def handleCloseSignal(closeSignal, isInLongPosition, isInShortPosition, handleCloseLong, handleCloseShort):
    if(closeSignal == SIGNALS.CLOSE.LONG):
        if(isInLongPosition == True):
            handleCloseLong()
        pass
    if(closeSignal == SIGNALS.CLOSE.SHORT):
        if(isInShortPosition == True):
            handleCloseShort()
        pass
    pass
