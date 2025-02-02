from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy.orm import Session
import crud, models, schemas
from typing import List
from pydantic import BaseModel
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Intento(BaseModel):
    letra: str
    palabra: str

@app.get("/imagen")
async def render_image():
    return FileResponse("static/imagen.jpg")

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

@app.post("/usuaris/", response_model=schemas.Usuari)
def create_usuari(usuari: schemas.UsuariCreate, db: Session = Depends(get_db)):
    return crud.create_usuari(db=db, usuari=usuari)

@app.get("/usuaris/{usuari_id}", response_model=schemas.Usuari)
def read_usuari(usuari_id: int, db: Session = Depends(get_db)):
    db_usuari = crud.get_usuari(db, usuari_id=usuari_id)
    if db_usuari is None:
        raise HTTPException(status_code=404, detail="Usuari not found")
    return db_usuari

@app.get("/usuaris/", response_model=List[schemas.Usuari])
def read_usuaris(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    usuaris = crud.get_usuaris(db, skip=skip, limit=limit)
    return usuaris
