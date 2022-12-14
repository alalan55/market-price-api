import fastapi

from models.ITask import Task

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
