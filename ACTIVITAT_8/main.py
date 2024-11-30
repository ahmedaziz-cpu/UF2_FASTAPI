from typing import Union, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


items: Dict[int, Item] = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "q": q, "item": items[item_id]}

@app.post("/items/")
async def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"id": item_id, **item.dict()}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"item_name": item.name, "item_id": item_id}