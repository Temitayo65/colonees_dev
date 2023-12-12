"""Add new user to admin table

Revision ID: de130b51aab2
Revises: 2cc7c0d1d320
Create Date: 2023-12-12 15:34:59.726276

"""
from typing import Sequence, Union
from sqlalchemy import Transaction, Transaction, Table, Column, String
from alembic import op
import sqlalchemy as sa
from app.config import settings
from sqlalchemy import text
from app.utils import hash


# revision identifiers, used by Alembic.
revision: str = 'de130b51aab2'
down_revision: Union[str, None] = '2cc7c0d1d320'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Add a new user to the admin table
    op.bulk_insert(
        sa.Table('administrators', sa.MetaData(), autoload_with=op.get_bind()),
        [
            {'email': f'{settings.admin_email}', 'password': f'{hash(settings.admin_password)}', "is_master" : True},
        ]
    )


def downgrade():
    op.execute(text("DELETE FROM administrators WHERE email = :email").bindparams(
        email=settings.admin_email))
