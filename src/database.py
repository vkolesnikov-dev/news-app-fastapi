from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///./news_site.db", connect_args={"check_same_thread": False},echo=True)
Session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



def get_db():
    """
    Зависимость для FastAPI - предоставляет сессию БД для каждого запроса
    """
    db = Session_local()
    try:
        yield db
    finally:
        db.close()