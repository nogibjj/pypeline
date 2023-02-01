"""
Function to read file into application based on file type
"""
import pandas as pd

# from dbcon import file

def create_data_object(file:str):
    """Created data object depending on file type"""
    #filetype = "csv"
    #if filetype == "csv":
    data_object = pd.read_csv(file)
    return data_object
