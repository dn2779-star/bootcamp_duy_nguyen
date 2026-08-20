import pandas as pd 
import numpy as np 
def fill_missing_median(df: pd.DataFrame, columns: list[str] = None) -> pd.DataFrame:
    df_copy = df.copy()
    if columns is None or columns not in list(df.columns):
        columns = df.select_dtypes(include=np.number).columns
    for col in columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy

def drop_missing(df: pd.DataFrame, threshold: int) -> pd.DataFrame:
    df_copy = df.copy()
    thresh = int(threshold * df.shape[1])
    df_copy = df_copy.dropna(thresh=thresh)
    return df_copy

def normalize(df: pd.DataFrame, columns: list[str] = None) -> pd.DataFrame:
    df_copy = df.copy()
    if columns is None or columns not in list(df.columns):
        columns = df.select_dtypes(include=np.number).columns
    for col in columns:
        df_copy[col] = (df_copy[col]-df_copy[col].mean())/df_copy[col].std()
    return df_copy
