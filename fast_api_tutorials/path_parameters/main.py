from fastapi import FastAPI

# An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over. https://docs.python.org/3.9/library/enum.html
from enum import Enum

# create a sub-class that inherits from str and from Enum. by inheriting from str the API docs will be able to know that the values must be of type string and will be able to render correctly. Capitalized values to clarify which part I'm referencing later.
class ModelName(str, Enum):
    alexnet = "Alexnet"
    resnet = "Resnet"
    lenet = "Lenet"
    # names of Machine Learning models

server = FastAPI()

@server.get("/")
async def root():
    return {"message": "Hello World!"}

# ENDPOINT WITH ROUTE PARAMETER
@server.get("/items/{item_id}")
async def read_item(item_id: int): # * see type notes at bottom
    return {"item_id": item_id}

    # note that number passed displays as int not string:
        # http://127.0.0.1:8000/items/5
        # {
        #     "item_id": 5
        # }

    # also note:
        # try with str or float after typing as int and you get:
        # http://127.0.0.1:8000/items/foo
        # {
        #     "detail": [
        #         {
        #             "loc": [
        #                 "path",
        #                 "item_id"
        #             ],
        #             "msg": "value is not a valid integer",
        #             "type": "type_error.integer"
        #         }
        #     ]
        # }

# PATH OPERATIONS ARE EVALUATED IN ORDER, so put /users/current first in the example below. otherwise, the path for /users/{user_id} would match also for /users/current, and evaluate a parameter user_id with a value of "current".
@server.get("users/current")
async def read_current_user():
    return {"user_id": "the current user"}

@server.get("users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# TYPE ANNOTATION USING ENUM
@server.get("/models/{model_name}")
# type annotation using the enum class created at top
async def get_model(model_name: ModelName):
    # value of route parameter will be an enumeration "member" ie. ModelName.alexnet, ModelName.lenet etc.
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "Lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

#  PATH CONVERTER - when you need the file path itself to contain a path
@server.get("/files/{file_path:path}") # :path means parameter should match any path
async def read_file(file_path: str):
    return {"file_path": file_path}
    # http://localhost:8000/files/johndoe/myfile.txt displays {"file_path": johndoe/myfile.txt}
    # http://localhost:8000/files/kylegilbert/myfile.txt displays {"file_path": "kylegilbert/myfile.txt"}