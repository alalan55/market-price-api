from typing import List
import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session
from interface.ITask import Task, TaskCreate
from db.config_db import get_db
from services.taskService import get_tasks, create_task

from interface.ITask import Task

router = fastapi.APIRouter()


@router.get("/task", response_model=List[Task])
async def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _users = get_tasks(db=db, skip=skip, limit=limit)
    return _users


@router.post("task/add", response_model=Task, status_code=201)
async def register_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db=db, task=task)


@router.patch("task/edit")
async def edit_task(task: Task):
    return {"result": []}


@router.delete("task/delete/{id}")
async def delete_task(id: int):
    return {"result": []}
