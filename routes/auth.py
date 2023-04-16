from fastapi import APIRouter, HTTPException, Depends, status
from passlib.context import CryptContext
from database import SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from jose import jwt, JWTError
from datetime import timedelta, datetime
import models


router = APIRouter(
    prefix="/auth", tags=["Auth"], responses={401: {"user": "Não autorizado"}})


SECRET_KEY = "KlgH6AzYDeZeGwD288to79I3vTHT8wp7"
ALGOTIGHTM = 'HS256'

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserLogin(BaseModel):
    email: str
    password: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def create_access_token(email: str, id: int, expires_delta: Optional[timedelta] = None):
    encode = {"sub": email, "id": id}

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})

    return jwt.encode(encode, SECRET_KEY, algorithm=ALGOTIGHTM)


def password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(password, hashed):
    return bcrypt_context.verify(password, hashed)


def authenticate_user(email: str, password: str, db):
    user = db.query(models.Users).filter(models.Users.email == email).first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


@router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(user.email, user.password, db)

    if not user:
        raise token_exception()

    token_expires = timedelta(minutes=60)
    token = create_access_token(
        user.email, user.id, expires_delta=token_expires)

    user.hashed_password = None
    return successful_response(200, token, user)


def token_exception():
    token_exception_resp = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Usuário ou senha icorretos", headers={"WWW-Authenticate": "Bearer"})
    return token_exception_resp


def successful_response(status_code: int, token: Optional[str] = None, content: Optional[dict or list] = None):
    return {
        "status": status_code,
        "message": "Sucesso!",
        "content": content,
        "token": token
    }
