"""empty message

Revision ID: 6aa632182386
Revises: 0a55ac4bf0dc
Create Date: 2023-04-21 16:50:04.827291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aa632182386'
down_revision = '0a55ac4bf0dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('website', schema=None) as batch_op:
        batch_op.alter_column('middle_data',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=3000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('website', schema=None) as batch_op:
        batch_op.alter_column('middle_data',
               existing_type=sa.String(length=3000),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=True)

    # ### end Alembic commands ###
