"""empty message

Revision ID: 680c7709331a
Revises: 340a574ac7ed
Create Date: 2019-12-30 22:01:04.450840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '680c7709331a'
down_revision = '340a574ac7ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_contests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('contest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contest_id'], ['contests.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_contests')
    # ### end Alembic commands ###
