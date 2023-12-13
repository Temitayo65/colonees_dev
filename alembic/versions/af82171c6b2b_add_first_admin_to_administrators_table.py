"""Add first Admin to Administrators table

Revision ID: af82171c6b2b
Revises: d9715a419373
Create Date: 2023-12-13 05:57:27.813137

"""
from typing import Sequence, Union
from sqlalchemy import Transaction, Transaction, Table, Column, String
from alembic import op
import sqlalchemy as sa
from app.config import settings
from sqlalchemy import text
from app.utils import hash


# revision identifiers, used by Alembic.
revision: str = 'af82171c6b2b'
down_revision: Union[str, None] = 'd9715a419373'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.bulk_insert(
        sa.Table('administrators', sa.MetaData(), autoload_with=op.get_bind()),
        [
            {'email': f'{settings.admin_email}',
                'password': f'{hash(settings.admin_password)}', "is_master": True},
        ]
    )


def downgrade():
    op.execute(text("DELETE FROM administrators WHERE email = :email").bindparams(
        email=settings.admin_email))
