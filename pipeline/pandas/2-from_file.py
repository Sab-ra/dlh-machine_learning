#!/usr/bin/env python3
"""Make data frame out of a file"""
import pandas as pd


def from_file(filename, delimiter):
    """Use CSV as uni filetype, make dataframe"""

    return pd.read_csv(filepath_or_buffer=filename,
                       delimiter=delimiter)
