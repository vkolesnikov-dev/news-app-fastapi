from datetime import datetime
from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    username: str
    email: str
    hashed_password: str
    avatar: str | None = None
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
