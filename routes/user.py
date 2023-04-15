from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Optional
from database import SessionLocal
from sqlalchemy.orm import Session
from routes.auth import password_hash
import models


class CreateUser(BaseModel):
    name: str
    email: str
    password: str
    profile_pic: Optional[str]


router = APIRouter(
    prefix="/user", tags=["User"]
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user_model = models.Users()
    user_model.name = user.name
    user_model.email = user.email
    user_model.hashed_password = password_hash(user.password)

    db.add(user_model)
    db.commit()

    return {"message": "Usuário criado com sucesso", "status": 201}
