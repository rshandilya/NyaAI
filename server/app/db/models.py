from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey
from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(String(80))
    is_admin = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"User(username={self.username}, is_admin={self.is_admin})"


