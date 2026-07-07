#!/usr/bin/env python3
"""Create Data Frame from ND-Array"""
#import numpy as np
import pandas as pd


def from_numpy(array):
    """columns will be labled a-z order"""
    
    col_count = array.shape[1]
    col_titles = [chr(i) for i in range(65, 65 + col_count)]

    return pd.DataFrame(array, columns=col_titles)
