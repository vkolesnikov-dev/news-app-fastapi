from sqlalchemy import Column, Integer, DATETIME
from src.database import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DATETIME(timezone=True))

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"