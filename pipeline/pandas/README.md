# Pandas

## Training Datasets

Training datasets located: '../datasets'

## 0-from_numpy.py

Write a function `def from_numpy(array):` that creates a **pd.DataFrame** from a np.ndarray:

- [x] array is the np.ndarray from which you should create the pd.DataFrame
- [x] The columns of the pd.DataFrame should be labeled in alphabetical order and capitalized. There will not be more than 26 columns.
- [x] Returns: the newly created pd.DataFrame

## 1-from_dictionary.py

Write a python **script** that creates a **pd.DataFrame from a dictionary**:

- [x] The first column should be labeled First and have the values 0.0, 0.5, 1.0, and 1.5
- [x] The second column should be labeled Second and have the values one, two, three, four
- [x] The rows should be labeled A, B, C, and D, respectively
- [x] The pd.DataFrame should be saved into the variable df

## 2-from_file.py

Write a function `def from_file(filename, delimiter):` that loads data from a file as a pd.DataFrame:

- [x]filename is the file to load from
- [x]delimiter is the column separator
- [x]Returns: the loaded pd.DataFrame

## 3-rename.py

Write a function `def rename(df):` that takes a pd.DataFrame as input and performs the following:

- [x] df is a pd.DataFrame containing a column named Timestamp.
- [x] The function should rename the Timestamp column to Datetime.
- [x] Convert the timestamp values to datetime values
- [x] Display only the Datetime and Close column
- [x] Returns: the modified pd.DataFrame

## 4-array.py

Write a function `def array(df):` that takes a pd.DataFrame as input and performs the following:

- [x] df is a pd.DataFrame containing columns named High and Close.
- [x] The function should select the last 10 rows of the High and Close columns.
- [x] Convert these selected values into a numpy.ndarray.
- [x] Returns: the numpy.ndarray
- [x] The function will be called from modules that already have pandas and numpy, so no need to import

## 5-slice.py

Write a function `def slice(df):` that takes a pd.DataFrame and:

- [ ] Extracts the columns High, Low, Close, and Volume_(BTC).
- [ ] Selects every 60th row from these columns.
- [ ] Returns: the sliced pd.DataFrame

## 6-flip_switch.py

Write a function `def flip_switch(df):` that takes a pd.DataFrame and:

- [x] Sorts the data in reverse chronological order.
- [x] Transposes the sorted dataframe (column Timestamp).
- [x] Returns: the transformed pd.DataFrame.

## 7-high.py

Write a function `def high(df):` that takes a pd.DataFrame and:

- [x] Sorts it by the High price in descending order.
- [x] Returns: the sorted pd.DataFrame.

## 8-prune.py

Write a function `def prune(df):` that takes a pd.DataFrame and:

- [x] Removes any entries where Close has NaN values.
- [x] Returns: the modified pd.DataFrame.

## 9-fill.py

Write a function `def fill(df):` that takes a pd.DataFrame and:

- [x] Removes the Weighted_Price column.
- [x] Fills missing values in the Close column with the previous row’s value.
- [x] Fills missing values in the High, Low, and Open columns with the corresponding Close value in the same row.
- [x] Sets missing values in Volume_(BTC) and Volume_(Currency) to 0.
- [x] Returns: the modified pd.DataFrame.

## 10-index.py

Write a function `def index(df):` that takes a pd.DataFrame and:

- [x] Sets the Timestamp column as the index of the dataframe.
- [x] Returns: the modified pd.DataFrame.

## 11-concat.py

Write a function `def concat(df1, df2):` that takes two pd.DataFrame objects and:

- [x] Indexes both dataframes on their Timestamp columns.
- [x] Includes all timestamps from df2 (bitstamp) up to and including timestamp 1417411920.
- [x] Concatenates the selected rows from df2 to the top of df1 (coinbase).
- [x] Adds keys to the concatenated data, labeling the rows from df2 as bitstamp and the rows from df1 as coinbase.
- [x] You should use `index = __import__('10-index').index`
- [x] Returns the concatenated pd.DataFrame.

## 12-hierarchy.py

Based on [11-concat.py], write a function `def hierarchy(df1, df2):` that takes two pd.DataFrame objects and:

- [x] Rearranges the MultiIndex so that Timestamp is the first level.
- [x] Concatenates the bitstamp and coinbase tables from timestamps 1417411980 to 1417417980, inclusive.
- [x] Adds keys to the data, labeling rows from df2 as bitstamp and rows from df1 as coinbase.
- [x] Ensures the data is displayed in chronological order.
- [x] You should use index = __import__('10-index').index.
- [x] Returns: the concatenated pd.DataFrame.

## 13-analyze.py

Write a function `def analyze(df):` that takes a pd.DataFrame and:

- [x] Computes descriptive statistics for all columns except the Timestamp column.
- [x] Returns a new pd.DataFrame containing these statistics.

## 14-visualize.py

Complete the following script to visualize the pd.DataFrame:

- [x] The column Weighted_Price should be removed

- [x] Rename the column Timestamp to Date

- [x] Convert the timestamp values to date values

- [ ] Index the data frame on Date

- [ ] Missing values in Close should be set to the previous row value

- [ ] Missing values in High, Low, Open should be set to the same row's Close value

- [ ] Missing values in Volume_(BTC) and Volume_(Currency) should be set to 0

- [ ] Plot the data from 2017 and beyond at daily intervals and group the values of the same day such that:

    - [ ] High: max
    - [ ] Low: min
    - [ ] Open: mean
    - [ ] Close: mean
    - [ ] Volume(BTC): sum
    - [ ] Volume(Currency): sum

- [ ] Return the transformed pd.DataFrame before plotting.

```python3
#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# YOUR CODE HERE
```
