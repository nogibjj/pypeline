"""
Module for api requests
"""
from fastapi import FastAPI
from src import extract

# import pandas as pd

app = FastAPI()


@app.post("/create")
async def create_pipeline(file: str):
    """function to get user data"""
    data_type = extract.find_file_type(file)
    data_object = extract.create_data_object(data_type, file)
    return data_object


def choose_transformation(data_object):
    """function to choose transformation to apply to data"""
    return data_object
