#!/usr/bin/env python3
"""Timestamp to DateTime"""
import pandas as pd


def rename(df):
    """Rename Timestampt to Datetime,
    and return only the Datetime and Close"""

    df = df.rename(columns={'Timestamp': 'Datetime'})
    df.Datetime = pd.to_datetime(df.Datetime, unit='s')

    return df[['Datetime', 'Close']]
