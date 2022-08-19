from pydantic import BaseModel


class Task(BaseModel):
    title: str
    quantity: int
    value: float
