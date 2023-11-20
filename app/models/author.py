from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)

    books = relationship("Book", back_populates="author")
