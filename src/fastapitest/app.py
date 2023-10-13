from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.api import add_user, get_all
from api.database import Base, engine, SessionLocal, Person
from api.user import User

# создаем таблицы
Base.metadata.create_all(bind=engine)

api_app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api_app.post("/test", response_model=User)
def main(user: User):
    # сохранить в базу user
    return user


@api_app.post("/api/users/add", response_model=User)
def add_an_employee(body: User, db: Session = Depends(get_db)) -> Person:
    return add_user(body, db)


@api_app.get("/api/users")
def entire_staff_list(db: Session = Depends(get_db)):
    return get_all(db)


@api_app.get("/api/users/{id}")
def employee_by_id(id, db: Session = Depends(get_db)):
    """Сотрудник по id"""
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    # если пользователь найден, отправляем его
    return person


@api_app.put("/api/surname/{id}/{surname}")
def edit_surname(id, surname, db: Session = Depends(get_db)):
    """меняем фамилию"""
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.surname = surname
    db.commit()  # сохраняем изменения
    db.refresh(person)
    return person


@api_app.put("/api/name/{id}/{name}")
def edit_name(id, name, db: Session = Depends(get_db)):
    """меняем имя"""
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.name = name
    db.commit()  # сохраняем изменения
    db.refresh(person)
    return person


@api_app.put("/api/salary/{id}/{salary}")
def edit_salary(id, salary, db: Session = Depends(get_db)):
    """меняем зарплату"""
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.salary = salary
    db.commit()  # сохраняем изменения
    db.refresh(person)
    return person


@api_app.delete("/api/users/{id}")
def delete_an_employee(id, db: Session = Depends(get_db)):
    """Удалить сотрудника"""
    # получаем пользователя по id
    person = db.query(Person).filter(Person.id == id).first()

    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})

    # если пользователь найден, удаляем его
    db.delete(person)  # удаляем объект
    db.commit()  # сохраняем изменения
    return person
