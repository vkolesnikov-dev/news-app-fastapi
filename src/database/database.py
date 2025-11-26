from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.config import settings

Base = declarative_base()

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)
Session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Зависимость для FastAPI - предоставляет сессию БД для каждого запроса
    """
    db = Session_local()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    Base.metadata.create_all(engine)
