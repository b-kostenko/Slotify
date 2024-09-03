from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.config import settings


def create_postgres_connection_string(host, port, username, password, database="") -> str:
    return f"postgresql://{username}:{password}@{host}:{port}/{database}"

SQLALCHEMY_DATABASE_URL = create_postgres_connection_string(
    host=settings.POSTGRES_HOST,
    port=settings.POSTGRES_PORT,
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    database=settings.POSTGRES_DATABASE,)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    echo_pool=False
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
