"""empty message

Revision ID: 0e6bd3c06008
Revises: 25a06dbd6e61
Create Date: 2021-06-04 16:53:12.987169

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0e6bd3c06008'
down_revision = '25a06dbd6e61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('login_history', sa.Column('last_time_login', sa.DateTime(), nullable=True))
    op.drop_column('login_history', 'last_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('login_history', sa.Column('last_time', mysql.DATETIME(), nullable=True))
    op.drop_column('login_history', 'last_time_login')
    # ### end Alembic commands ###
