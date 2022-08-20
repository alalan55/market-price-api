from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    quantity: int
    value: float

class TaskCreate(TaskBase):
    ...
    
class Task(TaskBase):
    id: int
    class Config:
        orm_mode = True
