import pandas_ta as ta
import yfinance as yf

# Request historic pricing data via finance.yahoo.com API
df = yf.Ticker('BTC-USD').history(period='1y')[['Close', 'Open', 'High', 'Volume']]

# Calculate MACD values using the pandas_ta library
df.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)

print(df)
