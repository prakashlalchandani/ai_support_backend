from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    """
    Central configuration for the application.

    All values are loaded from environment variables.
    The app MUST fail fast if critical values are missing.
    """

    # App
    APP_NAME: str = os.getenv("APP_NAME", "AI Support Backend")
    ENV: str = os.getenv("ENV", "development")

    # Database
    MONGO_URI: str = os.getenv("MONGO_URI")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")
    REDIS_URL: str = os.getenv("REDIS_URL")

    # Security / Auth
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    def validate(self):
        """Fail fast if required config is missing."""
        required = {
            "MONGO_URI": self.MONGO_URI,
            "DATABASE_NAME": self.DATABASE_NAME,
            "REDIS_URL": self.REDIS_URL,
            "SECRET_KEY": self.SECRET_KEY,
        }

        missing = [k for k, v in required.items() if not v]
        if missing:
            raise RuntimeError(
                f"Missing required environment variables: {', '.join(missing)}"
            )


settings = Settings()
settings.validate()
