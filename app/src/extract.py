"""
Function to read file into application based on file type
"""
import pandas as pd

# from dbcon import file


def find_file_type(file):
    """Detect file type"""
    if file.endswith(".csv"):
        filetype = "csv"
    elif file.endswith(".txt"):
        filetype = "txt"
    elif file.endswith(".parquet"):
        filetype = "parquet"
    else:
        print("File format not supported")
    return filetype


def create_data_object(filetype, file):
    """Created data object depending on file type"""
    if filetype == "csv":
        data_object = pd.read_csv(file)

    elif filetype == "txt":
        data_object = pd.read_csv(file, sep="\t")
    else:
        data_object = pd.read_parquet(file)
    return data_object
    