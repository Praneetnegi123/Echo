"""empty message

Revision ID: 825ff708bae1
Revises: 
Create Date: 2020-04-08 17:55:06.034692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '825ff708bae1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
