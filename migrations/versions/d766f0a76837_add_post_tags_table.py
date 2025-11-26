"""add post_tags table

Revision ID: d766f0a76837
Revises: 6c586f8791fb
Create Date: 2025-11-24 23:31:29.233431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd766f0a76837'
down_revision: Union[str, Sequence[str], None] = '6c586f8791fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'post_tags',
        sa.Column('post_id', sa.Integer, sa.ForeignKey('posts.id'), primary_key=True),
        sa.Column('tag_id', sa.Integer, sa.ForeignKey('tags.id'), primary_key=True),
        sa.Column('added_at', sa.DateTime(timezone=True), server_default=sa.func.now())
    )

def downgrade() -> None:
    """Downgrade schema."""

    op.drop_table('post_tags')
