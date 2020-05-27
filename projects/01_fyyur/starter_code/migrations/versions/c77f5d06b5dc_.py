"""empty message

Revision ID: c77f5d06b5dc
Revises: 99ce72c779ac
Create Date: 2020-05-18 23:12:41.124506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c77f5d06b5dc'
down_revision = '99ce72c779ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_Artist_name'), 'Artist', ['name'], unique=False)
    op.create_index(op.f('ix_Venue_name'), 'Venue', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Venue_name'), table_name='Venue')
    op.drop_index(op.f('ix_Artist_name'), table_name='Artist')
    # ### end Alembic commands ###
