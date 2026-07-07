#!/usr/bin/env python3
"""Define dictionare, lable rows: data frame"""
import pandas as pd


data_dictionary = {"First": [0.0, 0.5, 1.0, 1.5],
                   "Second": ['one', 'two', 'three', 'four']
                   }
row_lables = ['A', 'B', 'C', 'D']

df = pd.DataFrame(data=data_dictionary, index=row_lables)
