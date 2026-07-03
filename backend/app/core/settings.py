from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "BrainHint API"
    app_version: str = "0.1.0"
    database_url: str = "postgresql://brainhint:brainhint@localhost:5432/brainhint"
    cors_origins: list[str] = ["http://localhost:4200"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
