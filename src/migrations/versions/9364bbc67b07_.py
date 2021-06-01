"""empty message

Revision ID: 9364bbc67b07
Revises: 
Create Date: 2021-05-31 01:56:05.331733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9364bbc67b07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('likes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'likes')
    # ### end Alembic commands ###