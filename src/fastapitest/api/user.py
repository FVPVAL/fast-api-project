from datetime import date

from pydantic import BaseModel


class User(BaseModel):
    surname: str
    name: str
    salary: int

