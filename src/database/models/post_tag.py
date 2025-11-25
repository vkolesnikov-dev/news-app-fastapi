from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.database.models.base import BaseModel


class PostTag(BaseModel):
    __tablename__ = "post_tags"

    post_id = Column(Integer, ForeignKey('posts.id'),primary_key=True, index=True)
    tag_id = Column(Integer, ForeignKey('tags.id'),primary_key=True, index=True)
    added_by = Column(Integer, ForeignKey("users.id"))

