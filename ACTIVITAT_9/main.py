from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db_connect.database import get_db, Base, engine
from schemas.user import User
from crud.user import get_users

# Inicializar la aplicación de FastAPI
app = FastAPI()


# Endpoint para obtener todos los usuarios
@app.get("/users/", response_model=list[User])
def read_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users
