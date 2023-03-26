CREATE TABLE Student (
   student_id INT PRIMARY KEY,
   student_name VARCHAR(50) NOT NULL,
   student_address VARCHAR(100) NOT NULL,
   student_phone VARCHAR(20) NOT NULL,
   student_email VARCHAR(50) NOT NULL,
   student_department VARCHAR(50) NOT NULL,
   student_year INT NOT NULL
);

CREATE TABLE Hostel (
   hostel_id INT PRIMARY KEY,
   hostel_name VARCHAR(50) NOT NULL,
   hostel_address VARCHAR(100) NOT NULL,
   hostel_phone VARCHAR(20) NOT NULL
);

CREATE TABLE Room (
   room_id INT PRIMARY KEY,
   room_number VARCHAR(10) NOT NULL,
   room_capacity INT NOT NULL,
   hostel_id INT NOT NULL,
   FOREIGN KEY (hostel_id) REFERENCES Hostel(hostel_id)
);

CREATE TABLE Reservation (
   reservation_id INT PRIMARY KEY,
   start_date DATE NOT NULL,
   end_date DATE NOT NULL,
   student_id INT NOT NULL,
   room_id INT NOT NULL,
   FOREIGN KEY (student_id) REFERENCES Student(student_id),
   FOREIGN KEY (room_id) REFERENCES Room(room_id)
);
