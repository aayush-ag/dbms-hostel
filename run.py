import mysql.connector
from fastapi import FastAPI

# Replace the placeholders with your actual database credentials
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db"
)

app = FastAPI()

@app.post("/get/studentid")
def get_users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Student JOIN Reservation ON Student.student_id = Reservation.student_id JOIN Room ON Reservation.room_id = Room.room_id JOIN Hostel ON Room.hostel_id = Hostel.hostel_id WHERE Student.student_id = %s;", studentid)
    users = cursor.fetchall()
    return {"users": users}
