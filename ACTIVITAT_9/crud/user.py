from sqlalchemy.orm import Session
from models import User as UserModel

def get_users(db: Session):
    return db.query(UserModel).all()