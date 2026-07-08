#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

## Grooming
df = df.drop(['Weighted_Price'], axis=1)
df = df.rename(columns={'Timestamp': 'Date'})
df['Date'] = pd.to_datetime(df['Date'], yearfirst=True, unit='s')
df = df.set_index('Date')

## Filling missing Values
df['Close'] = df['Close'].ffill()
df['Open'] = df['Open'].fillna(df['Close'])
df['High'] = df['High'].fillna(df['Close'])
df['Low'] = df['Low'].fillna(df['Close'])
df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

## Filter
df17 = df.loc['2017-01-01 00:00:00':]

## Group & Resample at Daily Intervals
agg_rules = {
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
}
df_daily = df17.resample('D').agg(agg_rules)

## Plot on Two Subplots sharing the X-axis

fig, (ax1, ax2) = plt.subplots(2, 1, 
                               sharex=True,
                               figsize=(10,8))
### Price metrices
df_daily[['Open', 'High', 'Low', 'Close']].plot(ax=ax1)
ax1.set_ylabel('USD Price')
ax1.set_title('Coinbase Daily Prices')
### Volume metrices
df_daily[['Volume_(BTC)', 'Volume_(Currency)']].plot(ax=ax2)
ax2.set_ylabel('Trading Volume')
ax2.set_title('Coinbase Daily Volume')

plt.tight_layout()
plt.show()

