#!/usr/bin/env python3
"""Descriptive stats"""


def analyze(df):
    """Use describe"""

    return df.iloc([1:], axis=1).describe()
