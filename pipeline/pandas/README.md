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

- [ ] Removes the Weighted_Price column.
- [ ] Fills missing values in the Close column with the previous row’s value.
- [ ] Fills missing values in the High, Low, and Open columns with the corresponding Close value in the same row.
- [ ] Sets missing values in Volume_(BTC) and Volume_(Currency) to 0.
- [ ] Returns: the modified pd.DataFrame.
