from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base

class Usuari(Base):
    __tablename__ = "usuaris"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    correu_electronic = Column(String, unique=True, index=True)
    contrasenya = Column(String)
    data_creacio = Column(TIMESTAMP)