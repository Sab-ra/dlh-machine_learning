#!/usr/bin/env python3
"""Sort DF"""


def high(df):
    """Sort by High price descending"""

    return df.sort_values(by='High', ascending=False)