#!/usr/bin/env python3
"""Slice columns and get every 60 raw"""


def slice(df):
    """Extract columts High, Low, Close,
    and Volume_(BTC):
    returns every 60'th row"""

    return df[['High',
               'Low',
               'Close',
               'Volume_(BTC)'
               ]].iloc[::60]
