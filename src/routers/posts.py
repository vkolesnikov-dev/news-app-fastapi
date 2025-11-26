from typing import List

from sqlalchemy.orm import Session

from src.database.database import get_db
from src.posts.crud import get_all_posts
from src.posts.shemas import GetPosts
from fastapi import APIRouter, Depends

post_router = APIRouter()

@post_router.get("/", response_model=List[GetPosts])
async def read_all_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    post = get_all_posts(db, skip=skip, limit=limit)
    return post