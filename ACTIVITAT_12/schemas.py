from pydantic import BaseModel
from datetime import datetime

class UsuariBase(BaseModel):
    nom: str
    correu_electronic: str

class UsuariCreate(UsuariBase):
    contrasenya: str

class Usuari(UsuariBase):
    id: int
    data_creacio: datetime

    class Config:
        from_attributes = True  # Cambié orm_mode por from_attributes
