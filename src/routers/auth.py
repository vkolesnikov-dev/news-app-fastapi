from typing import Annotated, List

from fastapi import APIRouter
from fastapi.params import Depends

from src.users.schemas import GetUser
from ..auth.crud import get_current_user

auth_router = APIRouter()


@auth_router.get("/token", response_model=List[GetUser])
async def read_root(user: Annotated[GetUser, Depends(get_current_user)]) -> GetUser:
    return user
