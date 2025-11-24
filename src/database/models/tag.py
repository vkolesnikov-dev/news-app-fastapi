from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import relationship

from src.database.models.base import BaseModel


class Tag(BaseModel):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False)

    posts = relationship("Post", secondary="post_tags", back_populates="tags")


    def __repr__(self):
        return f"<Tag(id={self.id}, name='{self.name}')>"
