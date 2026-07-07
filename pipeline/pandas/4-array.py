#!/usr/bin/env python3
"""DataFrame to ndarray"""
import pandas as pd


def array(df):
    """Take last 10 rows and make array"""

    return df[['High', 'Close']].tail(10).to_numpy()
