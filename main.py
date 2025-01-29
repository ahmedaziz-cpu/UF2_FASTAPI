from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Definir un modelo de datos para los Body-Fields
class Item(BaseModel):
    nombre: str
    precio: float
    cantidad: int

# Crear una ruta que reciba Body-Fields
@app.post("/items/")
async def crear_item(item: Item):
    return {
        "nombre": item.nombre,
        "precio": item.precio,
        "cantidad": item.cantidad,
        "mensaje": "Item recibido correctamente"
    }


