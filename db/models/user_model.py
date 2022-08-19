from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..config_db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    task = relationship("Task", back_populates="owner")