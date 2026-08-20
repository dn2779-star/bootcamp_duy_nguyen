# Homework 5 
- Created two directories for storing data. Raw data are not be modified and stored in data/raw. Processed data are cleaned, modified, or derivatives of raw data, are stored in data/processed.
- The CSV raw data is synthetically made in the Notebook.
- Parquet files are unable to show its superior reading speed and storing size because the CSV is too small (711B vs 3kB).
- Files with prefix "sample" are produced by running codes line by line. Files with prefix "utils" are produced by the write_df function.

# Homework 6  
- Create three new functions: fill_missing_median, drop_missing, normalize, in the cleaning.py module store in src.
- fill_missing_median takes in a DataFrame, specified columns and replaced missing values with median. If columns are not specified or not from df, replaced all missing values from all numeric columns.
- drop_missing takes in a Dataframe and a threshold value. A threshold is the percentage of columns in a row that contains valid (non-missing) values. Return Dataframe with rows that passes the threshold.
- normalize takes in a DataFrame, specified columns and calculate their z-score normalization value. If no specified columns or columns that are not from df, return z-score of all numeric columns.
