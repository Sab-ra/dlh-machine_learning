# Pandas

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

- [ ] df is a pd.DataFrame containing a column named Timestamp.
- [ ] The function should rename the Timestamp column to Datetime.
- [ ] Convert the timestamp values to datetime values
- [ ] Display only the Datetime and Close column
- [ ] Returns: the modified pd.DataFrame
