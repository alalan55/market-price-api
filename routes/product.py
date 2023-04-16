from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from database import SessionLocal
from sqlalchemy.orm import Session
from routes.auth import get_current_user, get_user_exception
from dtos.responses_dto import success_response_model
import models


router = APIRouter(prefix="/product", tags=["Products"])


class ProductCreate(BaseModel):
    name: str
    price: float
    buy_date: str
    buy_month: str
    buy_year: str
    quantity: int
    type: int
    owner_id: int


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/")
async def get_all_products(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    if not user or user is None:
        raise get_user_exception()

    product_model = db.query(models.Products).filter(
        models.Products.owner_id == user.get("id")).all()

    return success_response_model(200, product_model)


@router.post("/create")
async def create_product(product: ProductCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    if user is None:
        raise get_user_exception()

    product_model = models.Products()
    product_model.name = product.name
    product_model.price = product.price
    product_model.buy_date = product.buy_date
    product_model.buy_month = product.buy_month
    product_model.buy_year = product.buy_year
    product_model.quantity = product.quantity
    product_model.type = product.type
    product_model.owner_id = user.get("id")

    db.add(product_model)
    db.commit()

    return success_response_model(201, product, "Produto criado com sucesso!")
