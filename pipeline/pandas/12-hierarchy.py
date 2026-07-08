#!/usr/bin/env python3
"""Concatenate 2 DF's and sort"""
import pandas as pd


def hierarchy(df1, df2):
    """MultiIndex"""
    index = __import__('10-index').index
    df1 = index(df1)
    df2 = index(df2)
    df1_filtered = df1.loc[1417411980:1417417980]
    df2_filtered = df2.loc[1417411980:1417417980]
    df = pd.concat([df1_filtered, df2_filtered],
                   keys=['bitstamp', 'coinbase'])
    return df.swaplevel(0, 1).sort_index()
