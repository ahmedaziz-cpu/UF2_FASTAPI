from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Intento(BaseModel):
    letra: str
    palabra: str

@app.get("/imagen")
async def render_image():
    return FileResponse("render.png")

@app.post("/nuevo_intento")
async def nuevo_intento(intento: Intento):
    return JSONResponse(content={"message": "Intento registrado", "data": intento.dict()})

@app.get("/abecedario")
async def abecedario():
    letras = list("abcdefghijklmnopqrstuvwxyzñç")
    return JSONResponse(content={"letras": letras})

@app.get("/jugador/{id}")
async def jugador(id: int):
    jugador_info = {
        "id": id,
        "nombre": f"Jugador {id}",
        "puntos_actuales": 100,
        "total_partidas": 10,
        "partidas_ganadas": 5,
        "partida_mas_puntos": 200
    }
    return JSONResponse(content=jugador_info)