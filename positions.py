from constants import POSITION_SIDES

def getIsInPosition(positions, symbol, positionSide):
    return any(el.symbol == symbol and el.positionSide == positionSide for el in positions)

def getIsInLongPosition(positions, symbol):
    return getIsInPosition(positions, symbol, POSITION_SIDES.LONG)

def getIsInShortPosition(positions, symbol):
    return getIsInPosition(positions, symbol, POSITION_SIDES.SHORT)
