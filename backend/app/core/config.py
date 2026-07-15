from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        extra="ignore"
    )
    PROJECT_NAME: str = "HanArchive"
    VERSION: str = "1.0.0"
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    JWT_ALGORITHM: str = "HS256"
    REDIS_URL: str
    STORAGE_PATH: str = "./storage"
    CORS_ORIGINS: list[str] = Field(
        default=["http://localhost:3000"]
    )
    
@lru_cache
def get_settings():
    return Settings()

settings = get_settings()