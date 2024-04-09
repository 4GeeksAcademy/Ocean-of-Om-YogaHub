"""empty message

Revision ID: 02f2a09f58a7
Revises: 77a8ea25730e
Create Date: 2024-04-08 23:34:14.261017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02f2a09f58a7'
down_revision = '77a8ea25730e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('date_of_birth')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_of_birth', sa.VARCHAR(length=120), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
