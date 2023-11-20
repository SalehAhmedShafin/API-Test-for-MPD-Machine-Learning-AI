from sqlalchemy.orm import Session
from ..models import Book

def create_book(db: Session, title: str, author_id: int):
    db_book = Book(title=title, author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, new_title: str, new_author_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db_book.title = new_title
        db_book.author_id = new_author_id
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
