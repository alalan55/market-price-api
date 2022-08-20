import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session
from interface.IUser import User, UserCrete
from db.config_db import get_db
from services.userService import register_user

router = fastapi.APIRouter()


@router.post("/user/register", response_model=User, status_code=201)
async def register_user(userCreate: UserCrete, db: Session = Depends(get_db)):
    return register_user(db=db, user=userCreate)
