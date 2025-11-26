from datetime import datetime
from pydantic import BaseModel, ConfigDict

from src.users.shemas import User


class GetPosts(BaseModel):
    id: int
    title: str
    content: str
    image: str | None = None
    created_at: datetime
    updated_at: datetime

    author: User

    model_config = ConfigDict(from_attributes=True)