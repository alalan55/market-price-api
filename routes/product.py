from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from database import SessionLocal
from sqlalchemy.orm import Session
from routes.auth import get_current_user, get_user_exception
from dtos.responses_dto import success_response_model
import models


router = APIRouter(prefix="/product")


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
