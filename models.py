from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    profile_pic = Column(String)

    products = relationship("Products", back_populates="owner")


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    buy_date = Column(DateTime)
    buy_month = Column(Integer)
    buy_year = Column(Integer)
    quantity = Column(Integer)
    type = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship('Users', back_populates="products")
