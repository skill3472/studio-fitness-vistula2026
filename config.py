from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env"
    )

    # Paths
    FRONT_DIRECTORY: Path = Path("public/")

    # Database
    DATABASE_URL: str = "sqlite:///./test.db"

    # Auth
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080 # 7 days by default
    JWT_ALGORITHM: str = "HS256"
    JWT_SECRET_KEY: str

settings = Settings()