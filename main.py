from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    producto: str
    descripcion: Optional[str] = None
    precio: int
    IVA: Optional[int] = None
    unidades: int
    tipo: str

@app.get("/")
def read_root():
    return {"message": "Hola mundo!!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in [1, 2, 3]:  #
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return {"item_id": item_id, "message": "Este es el ítem solicitado"}

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item creado", "item": item}
