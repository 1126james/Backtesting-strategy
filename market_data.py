from pycoingecko import CoinGeckoAPI
import pandas as pd

def get_market_data(token_id: str = 'harrypotterobamasonic10in', intervals: int = 30, currency: str = "usd") -> pd.DataFrame:
    cg = CoinGeckoAPI()
    token_id = token_id #harrypotterobamasonic10in
    intervals = 30 # 'daily' interval is available for 1 / 7 / 14 / 30 / 90 / 180 days only.
    ohlc = cg.get_coin_ohlc_by_id(id = token_id, vs_currency = currency, days = intervals)
    df = pd.DataFrame(ohlc, columns = ['date', 'Open', 'High', 'Low', 'Close'])
    df['date'] = pd.to_datetime(df['date'], unit = 'ms').dt.strftime('%Y-%m-%d %H:00')
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df

print(get_market_data())


