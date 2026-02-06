from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Medical Booking System"
    VERSION: str = "1.0.0"
    
    # Database
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str
    
    DATABASE_URL: Optional[str] = None
    
    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    # Telegram Bot
    TELEGRAM_BOT_TOKEN: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings()