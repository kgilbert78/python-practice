from fastapi import FastAPI
from typing import Optional

server = FastAPI()

fake_items_db = [
    {"item_name": "Foo"}, 
    {"item_name": "Bar"}, 
    {"item_name": "Baz"}
]

@server.get("/")
async def root():
    return {"message": "Hello World!"}

# When you declare other function parameters that are not part of the route parameters, they are automatically interpreted as query parameters.
@server.get("/items/")
# 0 & 10 are default parameters if not specified by query params
async def read_item(skip: int = 0, limit: int = 10): # types convert url string inputs to integers
    return fake_items_db[skip : skip + limit] 
    # slice fake_items_db[0:10] (10 from 0+10) or w/query param generated starting index & index to stop before
    
    # http://127.0.0.1:8000/items/?skip=0&limit=10 displays the fake_items_db list 1st 10 items - so does http://127.0.0.1:8000/items/ because of defaults
    
    # query param skip=1 displays it without the first item, skip=3 or more displays empty list ... limit=2 displays it without the last item, etc.
    
    # probably want to put a check on the front end to make sure that in the query the skip isn't more than the limit

# OPTIONAL PARAMETERS with Optional (imported above)
@server.get("/items-opt/{item_id}")
async def read_item_opt(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    else:
        return {"item_id": item_id}
    # item_id is a path parameter and q is not, so, it's a query parameter... access both with http://localhost:8000/items-opt/1?q=query (1 is item_id, query is q)

# TYPE CONVERSION
@server.get("/items-type-conv/{item_id}")
async def read_item_conv(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
        # python method to modify contents of dict: https://www.w3schools.com/python/ref_dictionary_update.asp
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

    # http://localhost:8000/items-type-conv/foo?q=updated&short=1 to send with q of "updated" and short of any truthy value. short=0, short=false or leave short off to get default False & description display

# MULTIPLE PATHS
@server.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

    # examples with user_id of 1:
    # format http://localhost:8000/users/1/items/2 for & description display but no q.
    # format http://localhost:8000/users/1/items/2?q=updated&short=true for q of "updated", no description

# REQUIRED QUERY PARAMS
@server.get("/required-items/{item_id}")
async def read_required_items(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

    # http://localhost:8000/required-items/foo?needy=yes  (error if leave off ?needy=value)

@server.get("/required-items2/{item_id}")
async def read_required_items2(item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

    # http://localhost:8000/required-items2/foo?needy=1
    # http://localhost:8000/required-items2/foo?needy=1&skip=1&limit=2