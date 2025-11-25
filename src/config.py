from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./news_site.db"

    class Config:
        env_file = ".env"

settings = Settings()