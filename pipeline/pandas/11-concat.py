#!/usr/bin/env python3
"""Concatenate 2 DF's"""
import pandas as pd


def concat(df1, df2):
    """Base on Timestamp as index"""

    index = __import__('10-index').index
    df1 = index(df1)
    df2 = index(df2)

    df2_filtered = df2.loc[:1417411920]
    df = pd.concat([df2_filtered, df1], keys=['bitstamp', 'coinbase'])

    return df
