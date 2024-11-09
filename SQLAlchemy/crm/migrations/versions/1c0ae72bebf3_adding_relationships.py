"""Adding relationships

Revision ID: 1c0ae72bebf3
Revises: afa75826418f
Create Date: 2024-11-09 15:29:26.665335

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c0ae72bebf3'
down_revision: Union[str, None] = 'afa75826418f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
