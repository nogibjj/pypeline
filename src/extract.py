"""
Function to read file into application based on file type
"""
import pandas as pd

# from dbcon import file


def find_file_type():
    """Detect file type"""
    filetype = "csv"
    return filetype


def create_data_object(filetype):
    """Created data object depending on file type"""
    if filetype == "csv":
        data_object = pd.read_csv(filetype)

    return data_object
