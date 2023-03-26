from database import get_db
from fastapi import APIRouter, Body, Query
from pydantic import BaseModel

router = APIRouter()

class Reservation(BaseModel):
    reservation_id: int
    start_date: str
    end_date: str
    student_id: int
    room_id: int


@router.post("/")
async def create_reservation(reservation: Reservation = Body(...)):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO Reservation (reservation_id, start_date, end_date, student_id, room_id) VALUES (%s, %s, %s, %s, %s)"
    values = (reservation.reservation_id, reservation.start_date, reservation.end_date, reservation.student_id, reservation.room_id)
    cursor.execute(query, values)
    db.commit()
    return {"message": "Reservation created successfully."}


@router.get("/{reservation_id}")
async def get_reservation(reservation_id: int):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Reservation WHERE reservation_id = %s"
    values = (reservation_id,)
    cursor.execute(query, values)
    reservation = cursor.fetchone()
    if not reservation:
        return {"error": "Reservation not found."}
    return {"reservation": reservation}


@router.put("/{reservation_id}")
async def update_reservation(reservation_id: int, reservation: Reservation = Body(...)):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE Reservation SET start_date = %s, end_date = %s, student_id = %s, room_id = %s WHERE reservation_id = %s"
    values = (reservation.start_date, reservation.end_date, reservation.student_id, reservation.room_id, reservation_id)
    cursor.execute(query, values)
    db.commit()
    return {"message": "Reservation updated successfully."}


@router.delete("/{reservation_id}")
async def delete_reservation(reservation_id: int):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM Reservation WHERE reservation_id = %s"
    values = (reservation_id,)
    cursor.execute(query, values)
    db.commit()
    return {"message": "Reservation deleted successfully."}

@router.get("/search")
async def search_reservations(
    reservation_id: int = Query(None),
    start_date: str = Query(None),
    end_date: str = Query(None),
    student_id: int = Query(None),
    room_id: int = Query(None)
):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Reservation WHERE "
    values = []
    if reservation_id is not None:
        query += "reservation_id = %s AND "
        values.append(reservation_id)
    if start_date is not None:
        query += "start_date = %s AND "
        values.append(start_date)
    if end_date is not None:
        query += "end_date = %s AND "
        values.append(end_date)
    if student_id is not None:
        query += "student_id = %s AND "
        values.append(student_id)
    if room_id is not None:
        query += "room_id = %s AND "
        values.append(room_id)
    if query.endswith("WHERE "):
        return {"error": "Please provide at least one search parameter."}
    query = query[:-5]
    cursor.execute(query, tuple(values))
    reservations = cursor.fetchall()
    return {"reservations": reservations}