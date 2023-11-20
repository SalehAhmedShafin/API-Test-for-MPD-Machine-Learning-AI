from sqlalchemy.orm import Session
from ..models import Author

def create_author(db: Session, full_name: str):
    db_author = Author(full_name=full_name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Author).offset(skip).limit(limit).all()

def update_author(db: Session, author_id: int, new_full_name: str):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author:
        db_author.full_name = new_full_name
        db.commit()
        db.refresh(db_author)
    return db_author

def delete_author(db: Session, author_id: int):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author:
        db.delete(db_author)
        db.commit()
    return db_author
