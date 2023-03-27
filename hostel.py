from database import get_db
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

class HostelCreateRequest(BaseModel):
    hostel_id: int
    hostel_name: str
    hostel_address: str
    hostel_phone: str

class HostelUpdateRequest(BaseModel):
    hostel_name: str = None
    hostel_address: str = None
    hostel_phone: str = None

router = APIRouter()

@router.post("/{hostel_id}")
async def get_hostid(hostel_id: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Hostel WHERE hostel_id = %s;", (hostel_id,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        # get the column names
        column_names = [d[0] for d in cursor.description]

        # create a dictionary with the column names as keys and the result as values
        hostel = dict(zip(column_names, result))

        return {"hostel": hostel}
    else:
        raise HTTPException(status_code=404, detail="Hostel not found")    

@router.post("/get")
async def get_hostels(page: int = 1, per_page: int = 10, sort_by: str = "hostel_name", order: str = "asc", search: str = None):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    offset = (page - 1) * per_page
    query = "SELECT * FROM Hostel"
    count_query = "SELECT COUNT(*) AS count FROM Hostel"
    if search:
        query += f" WHERE hostel_name LIKE '%{search}%' OR hostel_address LIKE '%{search}%'"
        count_query += f" WHERE hostel_name LIKE '%{search}%' OR hostel_address LIKE '%{search}%'"
    query += f" ORDER BY {sort_by} {order} LIMIT %s OFFSET %s;"
    values = (per_page, offset)
    cursor.execute(query, values)
    hostels = cursor.fetchall()
    cursor.execute(count_query)
    count = cursor.fetchone()["count"]
    cursor.close()    
    return {"hostels": hostels, "count": count}

@router.post("/create")
async def create_hostel(request: HostelCreateRequest):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO Hostel (hostel_id, hostel_name, hostel_address, hostel_phone) VALUES (%s, %s, %s, %s);"
    values = (request.hostel_id, request.hostel_name, request.hostel_address, request.hostel_phone)
    try:
        cursor.execute(query, values)
        db.commit()
        status = "Done"
    except Exception as err:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error: {err}")
    cursor.close()    
    return {"status": status}

@router.put("/update/{hostel_id}")
async def update_hostel(hostel_id: int, update_request: HostelUpdateRequest):
    db = get_db()
    cursor = db.cursor()
    update_query = "UPDATE Hostel SET "
    update_values = []
    if update_request.hostel_name is not None:
        update_query += "hostel_name = %s, "
        update_values.append(update_request.hostel_name)
    if update_request.hostel_address is not None:
        update_query += "hostel_address = %s, "
        update_values.append(update_request.hostel_address)
    if update_request.hostel_phone is not None:
        update_query += "hostel_phone = %s, "
        update_values.append(update_request.hostel_phone)
    update_query = update_query.rstrip(", ") + " WHERE hostel_id = %s;"
    update_values.append(hostel_id)
    cursor.execute(update_query, update_values)
    db.commit()
    cursor.close()
    return {"message": f"Hostel with ID {hostel_id} updated successfully"}

@router.delete("/{hostel_id}")
async def delete_hostel(hostel_id: int):
    db = get_db()
    cursor = db.cursor()
    delete_query = "DELETE FROM Hostel WHERE hostel_id = %s;"
    cursor.execute(delete_query, (hostel_id,))
    db.commit()
    cursor.close()
    return {"message": f"Hostel with ID {hostel_id} deleted successfully"}
