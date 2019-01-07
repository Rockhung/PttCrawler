"""edit datetime nullable

Revision ID: 3af39c6792c0
Revises: 6794412e2720
Create Date: 2018-12-26 17:16:52.557060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3af39c6792c0'
down_revision = '6794412e2720'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.alter_column('post_datetime',
               existing_type=sa.DATETIME(),
               nullable=True)

    with op.batch_alter_table('push', schema=None) as batch_op:
        batch_op.alter_column('push_datetime',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('push', schema=None) as batch_op:
        batch_op.alter_column('push_datetime',
               existing_type=sa.DATETIME(),
               nullable=False)

    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.alter_column('post_datetime',
               existing_type=sa.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###
