SELECT *
FROM Student
JOIN Reservation ON Student.student_id = Reservation.student_id
JOIN Room ON Reservation.room_id = Room.room_id
JOIN Hostel ON Room.hostel_id = Hostel.hostel_id
WHERE Student.student_id = '1';