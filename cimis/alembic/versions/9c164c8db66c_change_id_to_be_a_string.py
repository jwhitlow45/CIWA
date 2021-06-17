"""change id to be a string

Revision ID: 9c164c8db66c
Revises: 8e87ac56acc7
Create Date: 2021-06-17 16:47:42.198034

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '9c164c8db66c'
down_revision = '8e87ac56acc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('DailyRaw', 'Id',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('HourlyRaw', 'Id',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('HourlyRaw', 'Id',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('DailyRaw', 'Id',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
