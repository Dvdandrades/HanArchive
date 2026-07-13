import secrets
from datetime import datetime, timedelta
from jose import JWTError, jwt

from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException
from app.main import app

SECRET_KEY = "PLACEHOLDER"
ALGORITHM = "ALG_PLACEHOLDER"
ACCESS_TOKEN_EXPIRE_MINUTES = 0

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://hanarchive.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "password")
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return credentials.username

