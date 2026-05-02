from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Test & Deploy Lab"
    environment: str = "development"

    model_config = {"env_file": ".env"}