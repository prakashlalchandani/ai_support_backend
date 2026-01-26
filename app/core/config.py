from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "AI Support Backend")
    ENV = os.getenv("ENV", "Development")
    SECRET_KEY = os.getenv("SECRET_KEY", "change this in production")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()