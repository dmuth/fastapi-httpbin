
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


from apis import methods
from apis import request

app = FastAPI()
app.include_router(methods.router)
app.include_router(request.router)


#
# TODO:
#
# X Write some unit tests
#X HTTP Methods: delete, patch, post, put
#
# 3 Figure out how to group endpoints in docs (tags?)
# 4 Make main page go to docs
# Additional content on main page
# - Deploy to Deta
# - Next batch of docs
#
# 2 Status Codes


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
#def read_root():
async def read_root():
	return {"Hello": "World"}


@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
async def read_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


