"""empty message

Revision ID: 86c2414fade1
Revises: 
Create Date: 2023-04-26 17:12:19.435285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86c2414fade1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('author_id', sa.String(length=100), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('website_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['website_id'], ['website.id'], ),
    sa.PrimaryKeyConstraint('author_id')
    )
    op.create_table('tags',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=100), nullable=True),
    sa.Column('website_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['website_id'], ['website.id'], ),
    sa.PrimaryKeyConstraint('tag_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    op.drop_table('author')
    # ### end Alembic commands ###
