INTERVALS = {
  'DAY_1': '1d',
  'DAY_3': '3d',
  'HOUR_1': '1h',
  'HOUR_2': '2h',
  'HOUR_4': '4h',
  'HOUR_6': '6h',
  'HOUR_8': '8h',
  'HOUR_12': '12h',
  'MINUTE_1': '1m',
  'MINUTE_3': '3m',
  'MINUTE_5': '5m',
  'MINUTE_15': '15m',
  'MINUTE_30': '30m',
  'MONTH_1': '1M',
  'WEEK_1': '1w',
}

FUTURES_CONTRACT_STREAM_KEYS = {
  'e': 'EVENT_TYPE',
  'E': 'EVENT_TIME',
  'ps': 'PAIR',
  'ct': 'CONTRACT_TYPE',
  'k': 'KLINE',
  'k.t': 'KLINE_START_TIME',
  'k.T': 'KLINE_CLOSE_TIME',
  'k.i': 'INTERVAL',
  'k.f': 'FIRST_TRADE_ID',
  'k.L': 'LAST_TRADE_ID',
  'k.o': 'OPEN_PRICE',
  'k.c': 'CLOSE_PRICE',
  'k.h': 'HIGH_PRICE',
  'k.l': 'LOW_PRICE',
  'k.v': 'VOLUME',
  'k.n': 'NUMBER_OF_TRADES',
  'k.x': 'IS_KLINE_CLOSED',
  'k.q': 'QUOTE_ASSET_VOLUME',
  'k.V': 'TAKER_BUY_VOLUME',
  'k.Q': 'TAKER_BUY_QUOTE_ASSET_VOLUME',
  'k.B': 'IGNORE',
}

POSITION_SIDES = {
    'LONG': 'LONG',
    'SHORT': 'SHORT'
}

SIGNALS = {
    'OPEN': {
        'LONG': 'open long',
        'SHORT': 'open short',
    },
    'CLOSE': {
        'LONG': 'close long',
        'SHORT': 'close short',
    }
}

SYMBOLS = {
  'BTC': 'btc',
}

MARKETS = {
    '1': '' + SYMBOLS.BTC + INTERVALS.MINUTE_1
}
