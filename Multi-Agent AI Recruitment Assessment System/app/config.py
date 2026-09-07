from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    E2B_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()

DATABASE_URL = settings.DATABASE_URL
E2B_API_KEY = settings.E2B_API_KEY