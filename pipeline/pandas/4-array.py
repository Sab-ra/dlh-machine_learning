#!/usr/bin/env python3
"""Requires call from module that has
numpy and pandas"""


def array(df):
    """Take last 10 rows and make array"""

    return df[['High', 'Close']].tail(10).to_numpy()
