from fastapi import APIRouter, Body, Query, HTTPException
from pydantic import BaseModel
from database import get_db

class Student(BaseModel):
    student_id: int
    student_name: str
    student_address: str
    student_phone: str
    student_email: str
    student_department: str
    student_year: int

class StudentUpdateRequest(BaseModel):
    student_name: str = None
    student_address: str = None
    student_phone: str = None
    student_email: str = None
    student_department: str = None
    student_year: int = None

router = APIRouter()

@router.post("/create")
async def create_student(student: Student = Body(...)):
    db = get_db()
    cursor = db.cursor()
    insert_query = "INSERT INTO Student (student_id, student_name, student_address, student_phone, student_email, student_department, student_year) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    insert_values = (student.student_id, student.student_name, student.student_address, student.student_phone, student.student_email, student.student_department, student.student_year)
    cursor.execute(insert_query, insert_values)
    db.commit()
    cursor.close()
    return {"message": f"Student with ID {student.student_id} created successfully"}

@router.post("/get")
async def get_students(
    student_id: int = Query(None),
    student_name: str = Query(None),
    student_address: str = Query(None),
    student_phone: str = Query(None),
    student_email: str = Query(None),
    student_department: str = Query(None),
    student_year: int = Query(None)
):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Student WHERE "
    conditions = []
    if student_id:
        conditions.append(f"student_id = {student_id}")
    if student_name:
        conditions.append(f"student_name = '{student_name}'")
    if student_address:
        conditions.append(f"student_address = '{student_address}'")
    if student_phone:
        conditions.append(f"student_phone = '{student_phone}'")
    if student_email:
        conditions.append(f"student_email = '{student_email}'")
    if student_department:
        conditions.append(f"student_department = '{student_department}'")
    if student_year:
        conditions.append(f"student_year = {student_year}")
    if not conditions:
        raise HTTPException(status_code=400, detail="Please provide at least one search parameter.")
    query += " AND ".join(conditions)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()

    columns = [desc[0] for desc in cursor.description]
    students = []
    for row in rows:
        student = {}
        for i, column in enumerate(columns):
            student[column] = row[i]
        students.append(student)

    return {"students": students}

@router.put("/{student_id}")
async def update_student(student_id: int, update_request: StudentUpdateRequest):
    db = get_db()
    cursor = db.cursor()
    update_query = "UPDATE Student SET "
    update_values = []
    if update_request.student_name is not None:
        update_query += "student_name = %s, "
        update_values.append(update_request.student_name)
    if update_request.student_address is not None:
        update_query += "student_address = %s, "
        update_values.append(update_request.student_address)
    if update_request.student_phone is not None:
        update_query += "student_phone = %s, "
        update_values.append(update_request.student_phone)
    if update_request.student_email is not None:
        update_query += "student_email = %s, "
        update_values.append(update_request.student_email)
    if update_request.student_department is not None:
        update_query += "student_department = %s, "
        update_values.append(update_request.student_department)
    if update_request.student_year is not None:
        update_query += "student_year = %s, "
        update_values.append(update_request.student_year)
    update_query = update_query.rstrip(", ") + " WHERE student_id = %s;"
    update_values.append(student_id)
    cursor.execute(update_query, update_values)
    db.commit()
    cursor.close()
    return {"message": f"Student with ID {student_id} updated successfully"}

@router.delete("/{student_id}")
async def delete_student(student_id: int):
    db = get_db()
    cursor = db.cursor()
    delete_query = "DELETE FROM Student WHERE student_id = %s;"
    cursor.execute(delete_query, (student_id,))
    db.commit()
    cursor.close()    
    return {"message": f"Student with ID {student_id} deleted successfully"}