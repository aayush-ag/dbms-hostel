from fastapi import APIRouter, Query
from database import get_db

router = APIRouter()

@router.post("/")
def search_records(
    student_id: int = Query(None),
    student_name: str = Query(None),
    student_address: str = Query(None),
    student_phone: str = Query(None),
    student_email: str = Query(None),
    student_department: str = Query(None),
    student_year: int = Query(None),
    reservation_id: int = Query(None),
    start_date: str = Query(None),
    end_date: str = Query(None),
    room_id: int = Query(None),
    room_number: str = Query(None),
    room_capacity: int = Query(None),
    hostel_id: int = Query(None),
    hostel_name: str = Query(None),
    hostel_address: str = Query(None),
    hostel_phone: str = Query(None)
):
    db = get_db()    
    cursor = db.cursor()
    query = "SELECT * FROM Student JOIN Reservation ON Student.student_id = Reservation.student_id JOIN Room ON Reservation.room_id = Room.room_id JOIN Hostel ON Room.hostel_id = Hostel.hostel_id WHERE "
    conditions = []
    if student_id is not None:
        conditions.append(f"Student.student_id = {student_id}")
    if student_name is not None:
        conditions.append(f"Student.student_name = '{student_name}'")
    if student_address is not None:
        conditions.append(f"Student.student_address = '{student_address}'")
    if student_phone is not None:
        conditions.append(f"Student.student_phone = '{student_phone}'")
    if student_email is not None:
        conditions.append(f"Student.student_email = '{student_email}'")
    if student_department is not None:
        conditions.append(f"Student.student_department = '{student_department}'")
    if student_year is not None:
        conditions.append(f"Student.student_year = {student_year}")
    if reservation_id is not None:
        conditions.append(f"Reservation.reservation_id = {reservation_id}")
    if start_date is not None:
        conditions.append(f"Reservation.start_date = '{start_date}'")
    if end_date is not None:
        conditions.append(f"Reservation.end_date = '{end_date}'")
    if room_id is not None:
        conditions.append(f"Room.room_id = {room_id}")
    if room_number is not None:
        conditions.append(f"Room.room_number = '{room_number}'")
    if room_capacity is not None:
        conditions.append(f"Room.room_capacity = {room_capacity}")
    if hostel_id is not None:
        conditions.append(f"Hostel.hostel_id = {hostel_id}")
    if hostel_name is not None:
        conditions.append(f"Hostel.hostel_name = '{hostel_name}'")
    if hostel_address is not None:
        conditions.append(f"Hostel.hostel_address = '{hostel_address}'")
    if hostel_phone is not None:
        conditions.append(f"Hostel.hostel_phone = '{hostel_phone}'")
    
    query += " AND ".join(conditions)
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    return {"records": records}
