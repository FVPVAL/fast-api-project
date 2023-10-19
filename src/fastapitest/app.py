from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette import status

from api.api import add_user, get_all, get_id, update_partial
from api.database import Base, engine, SessionLocal
from api.user import StaffBase, StaffUpdatePartial
from fastapitest.api import api

# создаем таблицы
Base.metadata.create_all(bind=engine)

api_app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api_app.post("/api/users/add", response_model=StaffBase, status_code=status.HTTP_201_CREATED)
def add_an_employee(body: StaffBase, db: Session = Depends(get_db)):
    return add_user(body, db)


@api_app.get("/api/users")
def entire_staff_list(db: Session = Depends(get_db)):
    return get_all(db)


@api_app.get("/api/users/{employee_id}")
def employee_by_id(employee_id, db: Session = Depends(get_db)):
    return get_id(employee_id, db)


@api_app.patch("/api/user/{employee_id}", response_model=StaffBase)
def update_by_id(employee_id, body_update: StaffUpdatePartial, db: Session = Depends(get_db)):
    return update_partial(employee_id, body_update, db)


@api_app.delete("/api/user/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id, db: Session = Depends(get_db)):
    api.delete_employee(employee_id, db)
