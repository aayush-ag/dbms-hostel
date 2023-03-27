from fastapi import FastAPI, HTTPException, Form, Body
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from pydantic import BaseModel


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # Update this to only allow the origins you want to permit
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# User model
class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password_hash = get_password_hash(password)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hash: str):
    return pwd_context.verify(password, hash)

# JWT token generation
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(username: str):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": username, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# User database (in memory for demo purposes)
users_db = [
    User(username="user1", password="password1"),
    User(username="user2", password="password2"),
]

class User(BaseModel):
    username: str
    password: str

# Login endpoint
@app.post("/signin")
def login(user: User):
    for db_user in users_db:
        if db_user.username == user.username and verify_password(user.password, db_user.password_hash):
            access_token = create_access_token(username=db_user.username)
            return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Incorrect username or password")