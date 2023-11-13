"""create nuekid tables

Revision ID: 8c66efdb4667
Revises: 
Create Date: 2023-11-13 18:29:03.784269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c66efdb4667'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.String(), nullable=True),
    sa.Column('day', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('lat', sa.String(), nullable=True),
    sa.Column('long', sa.Integer(), nullable=True),
    sa.Column('img', sa.String(), nullable=True),
    sa.Column('location_type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('event_type', sa.String(), nullable=True),
    sa.Column('people_needed', sa.Integer(), nullable=True),
    sa.Column('space_available', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.Column('date_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['date_id'], ['dates.id'], name=op.f('fk_events_date_id_dates')),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], name=op.f('fk_events_location_id_locations')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_events_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    op.drop_table('users')
    op.drop_table('locations')
    op.drop_table('dates')
    # ### end Alembic commands ###