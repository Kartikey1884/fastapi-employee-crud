from sqlalchemy.orm import Session
import models, schemas 

def get_employees(db: Session):
    return db.query(models.Item).all()

def get_employee(db: Session, employee_id: int):
    return (
        db
        .query(models.Item)
        .filter(models.Item.id == employee_id)
        .first()
    )

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Item(
        name=employee.name,
        email=employee.email
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeUpdate):
    db_employee = get_employee(db, employee_id)
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee
