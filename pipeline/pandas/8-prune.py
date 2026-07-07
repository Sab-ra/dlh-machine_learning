#!/usr/bin/env python3
"""Remove entries based on NaN"""


def prune(df):
    """Del rows where Close is NaN"""

    return df.dropna(subset=Close)
