from pydantic_settings import BaseSettings
from pydantic import Field
import secrets


class Settings(BaseSettings):
    app_name: str = Field(default="FastAPI Lab", env="APP_NAME")
    environment: str = Field(default="development", env="ENVIRONMENT")
    database_url: str = Field(default="sqlite:///./app.db", env="DATABASE_URL")
    secret_key: str = Field(default=secrets.token_urlsafe(32), env="SECRET_KEY")

    @property
    def is_production(self) -> bool:
        return self.environment.lower() == "production"

    @property
    def is_development(self) -> bool:
        return self.environment.lower() == "development"

    model_config = {
        "env_file": ".env",
        "case_sensitive": False,
        "extra": "ignore"
    }