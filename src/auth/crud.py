from typing import Annotated

from fastapi.params import Depends

from src.users.schemas import GetUser
from src.auth.deps import oauth2_scheme


def fake_decode_token(token):
    return GetUser(
        username=token + "fakedecoded", email="john@example.com"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user
