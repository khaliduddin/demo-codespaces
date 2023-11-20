# References
# Understanding MACD -> https://www.alpharithms.com/moving-average-convergence-divergence-macd-031217/
# MACD in Python -> https://www.alpharithms.com/calculate-macd-python-272222/
# MACD indicator Rules
# MACD crossing above the centerline - Uptrend
# MACD crossing below the centerline - Downtrend
# MACD crossing above the signal line - Buy
# MACD crossing below the signal line - Sell

import pandas as pd
import pandas_ta as ta
import yfinance as yf

pd.set_option('mode.chained_assignment', None)

# Request historic pricing data via finance.yahoo.com API
df = yf.Ticker('BTC-USD').history(period='1y')[['Close', 'Open', 'High', 'Low', 'Volume']]

# Calculate MACD values using the pandas_ta library
df.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)
print(df.tail())
print('*************')
df_2 = yf.download(tickers=['BTC-USD'], period='1d', interval='15m', auto_adjust=True)[['Close', 'Open', 'High', 'Low', 'Volume']]
print(df_2.tail())
print('*************')
# calculate MACD on hourly chart
df_2.ta.macd(close='Close', fast=12, slow=26, signal=9, append=True)
print(df_2.dropna(axis='rows').tail())
