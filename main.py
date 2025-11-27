from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.database import create_tables
from src.routers import posts, users, auth


@asynccontextmanager
async def lifespan(_: FastAPI):
    await create_tables()
    yield
    print('Завершение работы')


def get_app() -> FastAPI:
    application = FastAPI(lifespan=lifespan)

    application.include_router(posts.post_router, prefix="/posts", tags=["posts"])
    application.include_router(users.user_router, prefix="/users", tags=["users"])
    application.include_router(auth.auth_router, prefix="/auth", tags=["auth"])

    return application


app = get_app()
