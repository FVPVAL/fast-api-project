from fastapitest.api.database import Person


def add_user(body, db):
    user = Person(**body.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all(db):
    """Весь список"""
    return db.query(Person).all()
