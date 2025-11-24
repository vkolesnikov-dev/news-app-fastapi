from sqlalchemy import Column, Integer, String, Text, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from src.database.models.base import BaseModel


class Post(BaseModel):

    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    image = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True))

    author = relationship("User", back_populates="posts")
    tags = relationship("Tag", back_populates="posts", secondary="post_tags")

    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}')>"