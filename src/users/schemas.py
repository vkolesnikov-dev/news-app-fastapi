from pydantic import BaseModel, ConfigDict


class GetUser(BaseModel):
    username: str
    email: str
    avatar: str | None = None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
