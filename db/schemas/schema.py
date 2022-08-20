from dataclasses import field
from typing import List, Optional, Generic, TypeVar
from unittest import result
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class UserSchema(BaseModel):
    name: Optional[str] = None

    class Config:
        orm_mode = True


class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)


class TaskSchema(BaseModel):
    title: Optional[str] = None
    quantity: Optional[int] = None
    value: Optional[float] = None


class RequestTask(BaseModel):
    parameter: TaskSchema = Field(...)


class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
