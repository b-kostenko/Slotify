import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_DATABASE: str = os.getenv("POSTGRES_DATABASE")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")


settings = Settings()
