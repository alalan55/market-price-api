from unicodedata import name
from sqlalchemy.orm import Session
from models.model import User
from ..schemas.schemas import UserSchema


def register_user(db: Session, user: UserSchema):
    _user = User(name=user.name)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user
