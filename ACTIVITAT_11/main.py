from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from typing import List, Optional
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar el directorio de imágenes estáticas
app.mount("/static", StaticFiles(directory="imatges"), name="static")

# Modelo para los intentos
class Intento(BaseModel):
    letra: str
    palabra: str
    error: Optional[str] = None  # Añadido para gestionar errores

# Variable para almacenar los intentos
intentos = []

# Endpoint para obtener una imagen (sirve un archivo estático desde el directorio montado)
@app.get("/imatges", tags=["Multimedia"])
async def render_image():
    return FileResponse("imatges/istockphoto-1333357575-612x612.jpg")

# Endpoint para registrar un nuevo intento
@app.post("/nuevo_intento", tags=["Juego"])
async def nuevo_intento(intento: Intento):
    if len(intento.letra) != 1:  # Validar que solo sea una letra
        intento.error = "La letra debe ser un solo carácter"
    intentos.append(intento.dict())  # Guardar el intento
    return JSONResponse(content={"message": "Intento registrado", "data": intento.dict()})

# Endpoint para mostrar los intentos realizados
@app.get("/intentos", tags=["Juego"])
async def mostrar_intentos():
    return JSONResponse(content={"intentos": intentos})

# Endpoint para mostrar el abecedario formateado
@app.get("/abecedario", tags=["Juego"])
async def abecedario():
    letras = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Ñ Ç"
    return JSONResponse(content={"letras": letras})

# Endpoint para renderizar textos específicos
@app.get("/render_text/començar_partida", tags=["Texto"])
async def render_comencar_partida():
    return JSONResponse(content={"texto": "Començar partida"})

@app.get("/render_text/espaciado", tags=["Texto"])
async def render_text_espaciado():
    texto = "C o m e n ç a r   p a r t i d a"
    return JSONResponse(content={"texto": texto})

# Endpoint para mostrar estadísticas del jugador
@app.get("/jugador/{id}", tags=["Jugador"])
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

# Endpoint para comenzar una nueva partida
@app.post("/comenzar_partida", tags=["Juego"])
async def comenzar_partida():
    return JSONResponse(content={"message": "Partida comenzada", "estado": "activa"})
