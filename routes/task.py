import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session
from interface.ITask import Task, TaskCreate

from interface.ITask import Task

router = fastapi.APIRouter()


@router.get("/task")
async def get_tasks():
    return {"result": []}


@router.post("task/add")
async def register_task(task: Task):
    return {"result": []}


@router.patch("task/edit")
async def edit_task(task: Task):
    return {"result": []}


@router.delete("task/delete/{id}")
async def delete_task(id: int):
    return {"result": []}
