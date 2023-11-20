from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .crud import book_crud, author_crud, client_crud
from .database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/")
def create_book(title: str, author_id: int, db: Session = Depends(get_db)):
    return book_crud.create_book(db, title=title, author_id=author_id)

@app.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    return book_crud.get_book(db, book_id=book_id)

@app.put("/books/{book_id}")
def update_book(book_id: int, new_title: str, new_author_id: int, db: Session = Depends(get_db)):
    return book_crud.update_book(db, book_id=book_id, new_title=new_title, new_author_id=new_author_id)

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return book_crud.delete_book(db, book_id=book_id)

@app.post("/authors/")
def create_author(full_name: str, db: Session = Depends(get_db)):
    return author_crud.create_author(db, full_name=full_name)

@app.get("/authors/{author_id}")
def read_author(author_id: int, db: Session = Depends(get_db)):
    return author_crud.get_author(db, author_id=author_id)

@app.put("/authors/{author_id}")
def update_author(author_id: int, new_full_name: str, db: Session = Depends(get_db)):
    return author_crud.update_author(db, author_id=author_id, new_full_name=new_full_name)

@app.delete("/authors/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    return author_crud.delete_author(db, author_id=author_id)

@app.post("/clients/")
def create_client(full_name: str, db: Session = Depends(get_db)):
    return client_crud.create_client(db, full_name=full_name)

@app.get("/clients/{client_id}")
def read_client(client_id: int, db: Session = Depends(get_db)):
    return client_crud.get_client(db, client_id=client_id)

@app.put("/clients/{client_id}")
def update_client(client_id: int, new_full_name: str, db: Session = Depends(get_db)):
    return client_crud.update_client(db, client_id=client_id, new_full_name=new_full_name)

@app.delete("/clients/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    return client_crud.delete_client(db, client_id=client_id)
