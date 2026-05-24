from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float
    is_active: bool = True