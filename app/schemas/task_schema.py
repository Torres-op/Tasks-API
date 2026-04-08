from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class StatusEnum(str, Enum):
    aguardando = "aguardando"
    em_progresso = "em_progresso"
    feito = "feito"

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(BaseModel):
    title: str = Field(examples=["Exemplo de Título"])
    description: str = Field(examples=["Exemplo de descrição"])
    status: StatusEnum = Field(examples=["aguardando"])
    priority: PriorityEnum = Field(examples=["low"])

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None
    priority: Optional[PriorityEnum] = None
