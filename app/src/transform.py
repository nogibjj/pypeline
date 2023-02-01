"""Function to do the data transformations"""
#import pandas as pd

def create_data_report(data_object):
    """function to create report about the data provided"""
    missing = missing_values(data_object)
    duplicate = duplicate_values(data_object)
    summary = summary_stats(data_object)
    return missing, duplicate, summary


def missing_values(data):
    """function to check missing values and return missing values stats"""
    # missing overall
    pre_len = data.shape[0]
    missing = data[data.isna().any(axis=1)]
    missing_len = missing.shape[0]
    percentage_missing = round((missing_len / pre_len) * 100, 2)

    # missing by cols
    nas_sums = []
    for column in data.columns:
        col_nas = data[data[column].isna()]
        nas_sums.append(len(col_nas))

    missing_cols = dict(zip(data.columns, nas_sums))
    return percentage_missing, missing_cols


def duplicate_values(data):
    """function to check duplicated values and return dupliacted values stats"""
    pre_len = data.shape[0]
    duplicates = data[data.duplicated()]
    duplicates_len = duplicates.shape[0]
    percentage_duplicates = round((duplicates_len / pre_len) * 100, 2)

    # mdup by cols
    dup_sums = []
    for column in data.columns:
        col_nas = data[data.duplicated([column])]
        dup_sums.append(len(col_nas))

    dup_cols = dict(zip(data.columns, dup_sums))
    return percentage_duplicates, dup_cols


def summary_stats(data):
    """function to create summary stats object"""
    cols = len(data.columns)
    rows = data.shape[0]
    cols_rows = {"columns": cols,"rows" : rows}
    data_desc = data.describe().to_dict()
    return cols_rows, data_desc


def remove_missing(data):
    """function to create summary stats object"""
    no_na_object = data.dropna()
    return no_na_object


def remove_dups(data, col, ref:str = "last"):
    """function to create summary stats object"""
    if ref == "last":
        no_dups_object = data.drop_duplicates(subset=[col], keep="last")
    else:
        # remove duplicates based on specific column(s)
        no_dups_object = data.drop_duplicates(subset=[col])
    return no_dups_object
