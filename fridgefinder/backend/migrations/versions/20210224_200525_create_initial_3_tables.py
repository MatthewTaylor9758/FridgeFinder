"""create initial 3 tables

Revision ID: 847780970cca
Revises: 
Create Date: 2021-02-24 20:05:25.731026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '847780970cca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('pantries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('foods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('amount', sa.String(), nullable=False),
    sa.Column('pantry_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pantry_id'], ['pantries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('foods')
    op.drop_table('pantries')
    op.drop_table('users')
    # ### end Alembic commands ###
