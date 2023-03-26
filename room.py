from database import get_db
from fastapi import APIRouter, Body, Query
from pydantic import BaseModel

router = APIRouter()

class Room(BaseModel):
    room_id: int
    room_number: str
    room_capacity: int
    hostel_id: int


@router.post("/")
async def create_room(room: Room = Body(...)):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO Room (room_id, room_number, room_capacity, hostel_id) VALUES (%s, %s, %s, %s)"
    values = (room.room_id, room.room_number, room.room_capacity, room.hostel_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return {"message": "Room created successfully."}


@router.get("/{room_id}")
async def get_room(room_id: int):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Room WHERE room_id = %s"
    values = (room_id,)
    cursor.execute(query, values)
    room = cursor.fetchone()
    if not room:
        return {"error": "Room not found."}
    cursor.close()
    return {"room": room}


@router.put("/{room_id}")
async def update_room(room_id: int, room: Room = Body(...)):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE Room SET room_number = %s, room_capacity = %s, hostel_id = %s WHERE room_id = %s"
    values = (room.room_number, room.room_capacity, room.hostel_id, room_id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return {"message": "Room updated successfully."}


@router.delete("/{room_id}")
async def delete_room(room_id: int):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM Room WHERE room_id = %s"
    values = (room_id,)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return {"message": "Room deleted successfully."}

@router.get("/search")
async def search_rooms(room_number: str = Query(None),
                       room_capacity: int = Query(None),
                       hostel_id: int = Query(None)):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Room WHERE 1=1"
    params = []
    if room_number:
        query += " AND room_number = %s"
        params.append(room_number)
    if room_capacity:
        query += " AND room_capacity = %s"
        params.append(room_capacity)
    if hostel_id:
        query += " AND hostel_id = %s"
        params.append(hostel_id)
    cursor.execute(query, tuple(params))
    rooms = cursor.fetchall()
    cursor.close()    
    return {"rooms": rooms}