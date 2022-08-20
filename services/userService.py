from sqlalchemy.orm import Session
from db.models import user_model
from db.schemas.schema import UserSchema


def register_user(user: UserSchema, db: Session):
    _user = user_model(name=user.name)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user
