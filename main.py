from fastapi import FastAPI, HTTPException
from models.employee import Employee

app = FastAPI()
employees_db = []

@app.get("/")
def root():
    return {"message": "Empleados API funcionando"}

@app.get("/employees")
def get_employees():
    return employees_db

@app.post("/employees", status_code=201)
def create_employee(employee: Employee):
    employees_db.append(employee)
    return employee

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for emp in employees_db:
        if emp.id == employee_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated: Employee):
    for i, emp in enumerate(employees_db):
        if emp.id == employee_id:
            employees_db[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for i, emp in enumerate(employees_db):
        if emp.id == employee_id:
            employees_db.pop(i)
            return {"message": f"Employee {employee_id} deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")