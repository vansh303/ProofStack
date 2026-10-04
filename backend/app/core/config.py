from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[3]

class Settings(BaseSettings):
    app_env: str = "development"
    app_secret: str

    backend_base_url: str = "https://localhost:8000"
    frontend_base_url: str = "https://localhost:3000"

    database_url: str
    redis_url: str

    github_client_id: str=""
    github_client_secret: str=""

    google_client_id: str = ""
    google_client_secret: str = ""

    ai_provider_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = Settings()