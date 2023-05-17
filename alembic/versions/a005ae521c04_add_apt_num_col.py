"""add apt num col

Revision ID: a005ae521c04
Revises: cc19b1ab44c4
Create Date: 2023-05-14 16:57:08.640647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a005ae521c04'
down_revision = 'cc19b1ab44c4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('address', sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('address', 'apt_num')
