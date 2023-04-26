"""empty message

Revision ID: 9f66ff92c123
Revises: 45a986ccb50b
Create Date: 2023-04-26 16:07:02.397314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f66ff92c123'
down_revision = '45a986ccb50b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'website', ['author'], ['author'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('author')

    # ### end Alembic commands ###
