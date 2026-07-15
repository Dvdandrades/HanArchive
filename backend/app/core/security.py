from datetime import datetime, timedelta, timezone
from typing import Any, Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

ALGORITHM = settings.jwt_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None, extra_claims: Optional[dict[str, Any]] = None) -> str:
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    payload = {
        "sub": subject,
        "exp": expire,
    }
    if extra_claims:
        payload.update(extra_claims)

    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)

def decode_access_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = decode_access_token(token)
    username = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return payload

def get_current_username(user: dict = Depends(get_current_user)) -> str:
    return user["sub"]

def require_role(role: str):
    def checker(user: dict = Depends(get_current_user)):
        roles = user.get("roles", [])
        if role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enought permits"
            )
        return user
    return checker