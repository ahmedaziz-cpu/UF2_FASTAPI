from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI()

# Montar el directorio de imágenes estáticas
app.mount("/static", StaticFiles(directory="imatges"), name="static")

# Tablas simuladas como diccionarios
jugadores_db = {}
partidas_db = {}
intentos_db = {}

# Modelos Pydantic
class Jugador(BaseModel):
    nombre: str
    puntos_actuales: int
    total_partidas: int
    partidas_ganadas: int
    partida_mas_puntos: int

class Partida(BaseModel):
    jugador_id: int
    puntos: int
    resultado: str

class Intento(BaseModel):
    partida_id: int
    letra: str
    palabra: str
    error: Optional[str] = None  # Añadido para gestionar errores

# Gestion de imagenes
@app.get("/imatges", tags=["Multimedia"])
async def render_image():
    image_path = os.path.join("imatges", "imatgefons.jpg")  # Aquí el nombre de la imagen
    if os.path.exists(image_path):
        return FileResponse(image_path)
    raise HTTPException(status_code=404, detail="Imagen no encontrada")

# Gestión del abecedario y textos específicos
@app.get("/abecedario", tags=["Juego"])
async def abecedario():
    letras = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Ñ Ç"
    return JSONResponse(content={"letras": letras})

@app.get("/render_text/començar_partida", tags=["Texto"])
async def render_comencar_partida():
    return JSONResponse(content={"texto": "Començar partida"})

@app.get("/render_text/espaciado", tags=["Texto"])
async def render_text_espaciado():
    texto = "C o m e n ç a r   p a r t i d a"
    return JSONResponse(content={"texto": texto})

# CRUD para la tabla Jugadores
@app.post("/jugadores/", tags=["Jugadores"])
async def crear_jugador(jugador: Jugador):
    id_nuevo = len(jugadores_db) + 1
    jugadores_db[id_nuevo] = jugador.dict()
    return {"id": id_nuevo, "jugador": jugador.dict()}

@app.get("/jugadores/", tags=["Jugadores"])
async def obtener_jugadores():
    return jugadores_db

@app.get("/jugadores/{id}", tags=["Jugadores"])
async def obtener_jugador(id: int):
    jugador = jugadores_db.get(id)
    if jugador:
        return jugador
    raise HTTPException(status_code=404, detail="Jugador no encontrado")

@app.put("/jugadores/{id}", tags=["Jugadores"])
async def actualizar_jugador(id: int, jugador: Jugador):
    if id in jugadores_db:
        jugadores_db[id] = jugador.dict()
        return {"id": id, "jugador": jugador.dict()}
    raise HTTPException(status_code=404, detail="Jugador no encontrado")

@app.delete("/jugadores/{id}", tags=["Jugadores"])
async def eliminar_jugador(id: int):
    if id in jugadores_db:
        del jugadores_db[id]
        return {"mensaje": "Jugador eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Jugador no encontrado")

# CRUD para la tabla Partidas
@app.post("/partidas/", tags=["Partidas"])
async def crear_partida(partida: Partida):
    id_nuevo = len(partidas_db) + 1
    partidas_db[id_nuevo] = partida.dict()
    return {"id": id_nuevo, "partida": partida.dict()}

@app.get("/partidas/", tags=["Partidas"])
async def obtener_partidas():
    return partidas_db

@app.get("/partidas/{id}", tags=["Partidas"])
async def obtener_partida(id: int):
    partida = partidas_db.get(id)
    if partida:
        return partida
    raise HTTPException(status_code=404, detail="Partida no encontrada")

@app.put("/partidas/{id}", tags=["Partidas"])
async def actualizar_partida(id: int, partida: Partida):
    if id in partidas_db:
        partidas_db[id] = partida.dict()
        return {"id": id, "partida": partida.dict()}
    raise HTTPException(status_code=404, detail="Partida no encontrada")

@app.delete("/partidas/{id}", tags=["Partidas"])
async def eliminar_partida(id: int):
    if id in partidas_db:
        del partidas_db[id]
        return {"mensaje": "Partida eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Partida no encontrada")

# CRUD para la tabla Intentos
@app.post("/intentos/", tags=["Intentos"])
async def crear_intento(intento: Intento):
    if len(intento.letra) != 1:  # Validar que la letra sea un solo caracter
        intento.error = "La letra debe ser un solo carácter"
    id_nuevo = len(intentos_db) + 1
    intentos_db[id_nuevo] = intento.dict()
    return {"id": id_nuevo, "intento": intento.dict()}

@app.get("/intentos/", tags=["Intentos"])
async def obtener_intentos():
    return intentos_db

@app.get("/intentos/{id}", tags=["Intentos"])
async def obtener_intento(id: int):
    intento = intentos_db.get(id)
    if intento:
        return intento
    raise HTTPException(status_code=404, detail="Intento no encontrado")

@app.put("/intentos/{id}", tags=["Intentos"])
async def actualizar_intento(id: int, intento: Intento):
    if id in intentos_db:
        intentos_db[id] = intento.dict()
        return {"id": id, "intento": intento.dict()}
    raise HTTPException(status_code=404, detail="Intento no encontrado")

@app.delete("/intentos/{id}", tags=["Intentos"])
async def eliminar_intento(id: int):
    if id in intentos_db:
        del intentos_db[id]
        return {"mensaje": "Intento eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Intento no encontrado")
