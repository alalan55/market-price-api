from sqlalchemy.orm import Session
from db.models.task_model import Task
from db.schemas import TaskSchema


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()
    # _user = User(name=user.name)
    # db.add(_user)
    # db.commit()
    # db.refresh(_user)
    # return _user


def create_task(db: Session, task: TaskSchema):
    _task = Task(title=task.title, quantity=task.quantity, value=task.value)
    db.add(_task)
    db.commit()
    db.refresh(_task)
    return _task
