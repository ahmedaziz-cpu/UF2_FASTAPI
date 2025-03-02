from fastapi import FastAPI
from typing import List
import read
import options_sch

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Benvingut a fastapi"}

# Ruta para obtener las opciones de temáticas
@app.get("/penjat/tematica/opcions", response_model=List[dict])
async def get_options():
    # Obtener las opciones de la base de datos
    options = read.read_db()
    return options_sch.options_schema(options)

# Ruta para obtener una palabra según el tema seleccionado
@app.get("/penjat/tematica/{option}", response_model=dict)
async def get_word(option: str):
    # Obtener la palabra asociada al tema
    word = read.read_word_db(option)
    print("IMPRESSIÓ WORD del mètode GET_WORD")
    print(type(word))
    print(word)
    return word