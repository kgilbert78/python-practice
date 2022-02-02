from fastapi import FastAPI

server = FastAPI()

# @ "decorator" takes the function below and does something with it. here it tells FastAPI that the function below corresponds to the path / with an operation get. more at https://realpython.com/primer-on-python-decorators/
@server.get("/")
async def root():
    # async not necessary but helps it run more efficiently. read more later: https://realpython.com/python-async-features/ and https://fastapi.tiangolo.com/async/#in-a-hurry
    return {"message": "Hello World!"}