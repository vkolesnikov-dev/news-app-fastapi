from sqlalchemy.orm import Session
from ..database.models.post import Post


def get_all_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()
