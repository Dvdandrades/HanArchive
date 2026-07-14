from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    database_url: str
    redis_url: str
    app_name: str = "HanArchive"
    debug: bool = False
    postgres_user: str
    postgres_pw: str
    postgres_db: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    secret_key: str
    

settings = Settings()