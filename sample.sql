-- Insert records into Student table
INSERT INTO Student (student_id, student_name, student_address, student_phone, student_email, student_department, student_year)
VALUES (1, 'John Doe', '123 Main St', '555-1234', 'john.doe@example.com', 'Computer Science', 3),
       (2, 'Jane Smith', '456 Park Ave', '555-5678', 'jane.smith@example.com', 'English', 2),
       (3, 'Bob Johnson', '789 Elm St', '555-9012', 'bob.johnson@example.com', 'History', 4);

-- Insert records into Hostel table
INSERT INTO Hostel (hostel_id, hostel_name, hostel_address, hostel_phone)
VALUES (1, 'Main Hostel', '123 Main St', '555-1234'),
       (2, 'Park Hostel', '456 Park Ave', '555-5678'),
       (3, 'Elm Hostel', '789 Elm St', '555-9012');

-- Insert records into Room table
INSERT INTO Room (room_id, room_number, room_capacity, hostel_id)
VALUES (1, '101', 2, 1),
       (2, '102', 4, 1),
       (3, '201', 2, 2),
       (4, '202', 3, 2),
       (5, '301', 1, 3),
       (6, '302', 2, 3);

-- Insert records into Reservation table
INSERT INTO Reservation (reservation_id, start_date, end_date, student_id, room_id)
VALUES (1, '2023-03-15', '2023-03-20', 1, 1),
       (2, '2023-03-18', '2023-03-23', 2, 3),
       (3, '2023-03-20', '2023-03-25', 3, 5);
