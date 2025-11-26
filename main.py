from fastapi import FastAPI
from src.routers import posts, users

app = FastAPI()

app.include_router(posts.post_router, prefix="/posts", tags=["posts"])
app.include_router(users.user_router, prefix="/users", tags=["users"])

@app.get("/")
async def read_root():
    return {"Hello": "World"}
