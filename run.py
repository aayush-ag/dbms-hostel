from fastapi import FastAPI
from hostel import router as hostel_router
from student import router as student_router
from reservation import router as reservation_router
from room import router as room_router
from search import router as search_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ["http://localhost:3000", "http://localhost:8081"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hostel_router, prefix="/hostels")
app.include_router(student_router, prefix="/student")
app.include_router(reservation_router, prefix="/reservation")
app.include_router(room_router, prefix="/room")
app.include_router(search_router, prefix="/search")


