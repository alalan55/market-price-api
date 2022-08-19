from sqlalchemy.orm import Session
from models.model import Task
from ..schemas.schemas import TaskSchema


def get_tasks(db: Session, task: TaskSchema, skip:int=0, limit:int=100):
    return db.query(Task).offset(skip).limit(limit).all()
    # _user = User(name=user.name)
    # db.add(_user)
    # db.commit()
    # db.refresh(_user)
    # return _user
