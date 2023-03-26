INSERT INTO Student (student_id, student_name, student_address, student_phone, student_email, student_department, student_year)
VALUES
  (1, 'Aayush Gupta', '123 Main Street, Delhi', '9876543210', 'aayush.gupta@example.com', 'Electronic Engg', 2),
  (2, 'Aliza Salim', '456 Park Avenue, Mumbai', '9876543211', 'aliza.salim@example.com', 'CSE', 3),
  (3, 'Md Hammad Akram', '789 Broadway, Bangalore', '9876543212', 'hammad.akram@example.com', 'CSE', 4),
  (4, 'Md Nabeel Ashar', '1011 Wall Street, Hyderabad', '9876543213', 'nabeel.ashar@example.com', 'CSE', 1),
  (5, 'Mohd Azim', '1213 Park Lane, Chennai', '9876543214', 'mohd.azim@example.com', 'CSE', 3),
  (6, 'Mohd Noman Khan', '1415 Elm Street, Kolkata', '9876543215', 'noman.khan@example.com', 'CSE', 2),
  (7, 'Rumman Ahmad', '1617 Main Road, Pune', '9876543216', 'rumman.ahmad@example.com', 'CSE', 1),
  (8, 'Saud Anwar', '1819 Market Street, Ahmedabad', '9876543217', 'saud.anwar@example.com', 'CSE', 2);

INSERT INTO Hostel (hostel_id, hostel_name, hostel_address, hostel_phone)
VALUES
  (1, 'Student C Hostel', '123 Main Street, Delhi', '011-23456789'),
  (2, 'The Student Hostel', '456 Park Avenue, Mumbai', '022-34567890'),
  (3, 'My Hostel', '789 Broadway, Bangalore', '080-45678901');

INSERT INTO Room (room_id, room_number, room_capacity, hostel_id)
VALUES
  (1, '101', 2, 1),
  (2, '102', 2, 1),
  (3, '201', 3, 2),
  (4, '202', 3, 2),
  (5, '301', 4, 3),
  (6, '302', 4, 3);

INSERT INTO Reservation (reservation_id, start_date, end_date, student_id, room_id)
VALUES
  (1, '2023-03-01', '2023-04-07', 1, 1),
  (2, '2023-03-15', '2023-05-20', 2, 3),
  (3, '2023-03-10', '2023-04-15', 3, 4),
  (4, '2023-03-01', '2023-06-10', 4, 6),
  (5, '2023-03-20', '2023-04-25', 5, 5),
  (6, '2023-02-01', '2023-05-10', 6, 2),
  (7, '2023-01-15', '2023-06-20', 7, 3),
  (8, '2022-12-05', '2023-04-09', 8, 1);
