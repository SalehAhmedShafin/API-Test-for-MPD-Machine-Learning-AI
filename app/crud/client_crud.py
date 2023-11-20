from sqlalchemy.orm import Session
from ..models import Client

def create_client(db: Session, full_name: str):
    db_client = Client(full_name=full_name)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def get_clients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Client).offset(skip).limit(limit).all()

def update_client(db: Session, client_id: int, new_full_name: str):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client:
        db_client.full_name = new_full_name
        db.commit()
        db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client:
        db.delete(db_client)
        db.commit()
