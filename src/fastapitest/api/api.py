from fastapi import HTTPException, status

from fastapitest.api.database import Person
from fastapitest.api.user import Staff, StaffUpdatePartial


def add_user(body, staff_db):
    user = Person(**body.model_dump())
    staff_db.add(user)
    staff_db.commit()
    staff_db.refresh(user)
    return user


def get_all(staff_db):
    """Весь список"""
    return staff_db.query(Person).all()


def get_id(employee_id, staff_db):
    person = staff_db.query(Person).filter(Person.id == employee_id).first()
    if person is not None:
        return person
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"employee_id: {employee_id} not found!")
# return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})


def update_partial(employee_id, body_update: StaffUpdatePartial, staff_db):
    employee = get_id(employee_id, staff_db)
    for name, value in body_update.model_dump(exclude_unset=True).items():
        setattr(employee, name, value)
    staff_db.commit()
    return employee


def delete_employee(employee_id, staff_db):
    employee = get_id(employee_id, staff_db)
    staff_db.delete(employee)
    staff_db.commit()

