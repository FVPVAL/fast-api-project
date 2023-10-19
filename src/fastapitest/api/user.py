from pydantic import BaseModel, ConfigDict


class StaffBase(BaseModel):
    surname: str
    name: str
    salary: int


class StaffUpdatePartial(StaffBase):
    surname: str | None = None
    name: str | None = None
    salary: int | None = None


class Staff(StaffBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    date: str

