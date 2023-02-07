"""
Function to read file(csv) into application based on file type
"""
import pandas as pd

def create_data_object(file:str):
    """Created data object depending on file type"""
    data_object = pd.read_csv(file)
    return data_object
