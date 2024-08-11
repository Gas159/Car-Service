"""add relationship company and service

Revision ID: 5f865dbab722
Revises: 4fc1d607508c
Create Date: 2024-08-11 19:17:43.113651

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5f865dbab722"
down_revision: Union[str, None] = "4fc1d607508c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "services", sa.Column("company_id", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        op.f("fk_services_company_id_companies"),
        "services",
        "companies",
        ["company_id"],
        ["id"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("fk_services_company_id_companies"),
        "services",
        type_="foreignkey",
    )
    op.drop_column("services", "company_id")
    # ### end Alembic commands ###