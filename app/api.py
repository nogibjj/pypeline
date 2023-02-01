"""
Module for api requests
"""
# import re
from fastapi import FastAPI
from src import read
from src import transform


app = FastAPI()

data_hold = []


@app.post("/load")
async def create_pipeline(file: str):
    """function to get user data"""
    data = read.create_data_object(file)
    data_hold.append(data)
    return {"message": "Data successfully uploaded"}


@app.get("/summary")
async def data_summary():
    """function to create data summary"""
    data = data_hold[0]
    load_summary = transform.create_data_report(data)
    return load_summary


@app.get("/extract/{task}")
async def choose_transformation(task: str):
    """function to choose transformation to apply to data"""
    data = data_hold[0]
    # match = re.search(r"\bmissing\b", task)
    if task == "missing":
        if task.endswith("all"):
            clean = transform.remove_missing(data, "all")
        else:
            clean = transform.remove_missing(data)
    else:
        # match = re.search(r"\bduplicate\b", task)
        col = task[2]
        if task.endswith("last"):
            clean = transform.remove_dups(data, col, "last")
        else:
            clean = transform.remove_dups(data, col)
    return clean


@app.get("/extract")
async def extract(formatted_object: object):
    """function to to return formatted data as csv"""
    return formatted_object
