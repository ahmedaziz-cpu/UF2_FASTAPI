from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Persona(BaseModel):
    nombre_completo: str
    edad: int
    contacto: str 

@app.post("/persona/")
async def crear_persona(persona: Persona):
    return {"mensaje": "Persona creada exitosamente", "datos_persona": persona}

class Ubicacion(BaseModel):
    calle: str
    ciudad: str
    pais: str

class PersonaConUbicacion(BaseModel):
    nombre_completo: str
    edad: int
    contacto: str  
    ubicacion: Ubicacion  

@app.post("/persona-con-ubicacion/")
async def crear_persona_con_ubicacion(persona: PersonaConUbicacion):
    return {"mensaje": "Persona con ubicación creada exitosamente", "detalles_persona": persona}
