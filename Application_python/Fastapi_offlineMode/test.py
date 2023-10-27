import asyncio
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import sqlite3

# SQLite

class EmpBase(BaseModel):
    id: int
    EmpName: str
    Grade: str

class my_db:
    @staticmethod
    def create_connect():
        conn = sqlite3.connect("Employee.db")
        return conn

    @staticmethod
    def register(emp: EmpBase):
        conn = my_db.create_connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Employees(id, Name, Grade) VALUES (?, ?, ?)",
            (emp.id, emp.EmpName, emp.Grade),
        )
        conn.commit()
        emp_id = cursor.lastrowid
        conn.close()
        return emp_id

    @staticmethod
    def get_all():
        conn = my_db.create_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employees")
        data = cursor.fetchall()
        conn.close()
        return data

    @staticmethod
    def get_by_id(id: int):
        conn = my_db.create_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employees WHERE id=?", (id,))
        data = cursor.fetchone()
        conn.close()
        return data

# FastAPI service
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <a href='http://localhost:8000/docs'>See document</a>
    </body>
    </html>
    """

@app.get("/employees")
def get_all_employee():
    return my_db.get_all()

@app.get("/employee/{employee_id}")
def get_employee(employee_id: int):
    return my_db.get_by_id(employee_id)
    # data = my_db.get_by_id(employee_id)
    # if data:
    #     return data
    # return {"message": "Employee not found"}

@app.post("/employee")
def register_employee(emp: EmpBase):
    emp_id = my_db.register(emp)
    return {"id":emp_id, **emp.model_dump()}

@app.put("/employee/{employee_id}")
def update_employee(employee_id: int, updated_emp: EmpBase):
    conn = my_db.create_connect()
    cursor = conn.cursor()
    
    # Check if the employee with the given ID exists
    cursor.execute("SELECT * FROM Employees WHERE id=?", (employee_id,))
    existing_employee = cursor.fetchone()
    
    if existing_employee:
        # Update the employee's information
        cursor.execute(
            "UPDATE Employees SET Name=?, Grade=? WHERE id=?",
            (updated_emp.EmpName, updated_emp.Grade, employee_id),
        )
        conn.commit()
        conn.close()
        return {"message": "Employee updated successfully"}
    
    conn.close()
    return {"message": "Employee not found"}

# Delete an employee by ID
@app.delete("/employee/{employee_id}")
def delete_employee(employee_id: int):
    conn = my_db.create_connect()
    cursor = conn.cursor()
    
    # Check if the employee with the given ID exists
    cursor.execute("SELECT * FROM Employees WHERE id=?", (employee_id,))
    existing_employee = cursor.fetchone()
    
    if existing_employee:
        # Delete the employee
        cursor.execute("DELETE FROM Employees WHERE id=?", (employee_id,))
        conn.commit()
        conn.close()
        return {"message": "Employee deleted successfully"}
    
    conn.close()
    return {"message": "Employee not found"}


# Creating the table if it doesn't exist
def create_table():
    conn = sqlite3.connect("Employee.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Employees (
            id INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            GRADE TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

#???

# @app.get("hello", response_class=HTMLResponse)
# def hello(request: Request):
#     return templates.TemplateResponse("hello.html", context={})


if __name__ == "__main__":
    create_table()  # Create the table if it doesn't exist
    config = uvicorn.Config(app)
    server = uvicorn.Server(config)
    uvicorn.run(app, host="localhost", port=8000)