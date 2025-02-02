from sqlalchemy.orm import Session
import models, schemas

def get_usuari(db: Session, usuari_id: int):
    return db.query(models.Usuari).filter(models.Usuari.id == usuari_id).first()

def get_usuaris(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Usuari).offset(skip).limit(limit).all()

def create_usuari(db: Session, usuari: schemas.UsuariCreate):
    db_usuari = models.Usuari(**usuari.dict())
    db.add(db_usuari)
    db.commit()
    db.refresh(db_usuari)
    return db_usuari