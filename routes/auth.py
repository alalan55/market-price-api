from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from database import SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
import models


router = APIRouter(
    prefix="/auth", tags=["Auth"], responses={401: {"user": "Não autorizado"}})


SECRET_KEY = "KlgH6AzYDeZeGwD288to79I3vTHT8wp7"
ALGOTIGHTM = 'HS256'

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CreateUser(BaseModel):
    name: str
    email: str
    password: str
    profile_pic: Optional[str]


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def password_hash(password):
    return bcrypt_context.hash(password)


@router.post("/user/create")
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user_model = models.Users()
    user_model.name = user.name
    user_model.email = user.email
    user_model.hashed_password = password_hash(user.password)

    db.add(user_model)
    db.commit()

    return {'message': 'Usuário criado com sucesso!'}
