from datetime import datetime
from pydantic import BaseModel, ConfigDict

from src.users.schemas import GetUser


class GetPosts(BaseModel):
    id: int
    title: str
    content: str
    image: str | None = None
    created_at: datetime
    updated_at: datetime

    author: GetUser

    model_config = ConfigDict(from_attributes=True)
