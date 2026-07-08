#!/usr/bin/env python3
"""Fill missing data in coin_df"""


def fill(df):
    """
    - [x] Drop column
    - [x] Fill NaN's
    """

    df = df.drop(['Weighted_Price'], axis=1)
    df['Close'] = df['Close'].ffill()
    df['Open'] = df['Open'].fillna(df['Close'])
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])

    return df
