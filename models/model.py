from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..db.config_db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    task = relationship("Task", back_populates="owner", useList=False)


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    value = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", nullable=False))

    owner = relationship("User", back_populates="task")
