"""empty message

Revision ID: 012efd05dc96
Revises: 8cc67dbe86b0
Create Date: 2023-02-07 13:39:55.249585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '012efd05dc96'
down_revision = '8cc67dbe86b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.Column('state', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=False),
    sa.Column('image_link', sa.String(length=500), nullable=False),
    sa.Column('website_link', sa.String(length=240), nullable=True),
    sa.Column('facebook_link', sa.String(length=240), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=False),
    sa.Column('seeking', sa.Boolean(), nullable=True),
    sa.Column('seeking_comment', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.Column('state', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=False),
    sa.Column('image_link', sa.String(length=500), nullable=False),
    sa.Column('website_link', sa.String(length=240), nullable=True),
    sa.Column('facebook_link', sa.String(length=240), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=False),
    sa.Column('seeking', sa.Boolean(), nullable=True),
    sa.Column('seeking_comment', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    with op.batch_alter_table('shows', schema=None) as batch_op:
        batch_op.drop_constraint('shows_venue_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('shows_artist_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'artists', ['artist_id'], ['id'])
        batch_op.create_foreign_key(None, 'venues', ['venue_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shows', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('shows_artist_id_fkey', 'artists', ['artist_id'], ['id'])
        batch_op.create_foreign_key('shows_venue_id_fkey', 'venues', ['venue_id'], ['id'])

    op.create_table('venues',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=False),
    sa.Column('website_link', sa.VARCHAR(length=240), autoincrement=False, nullable=True),
    sa.Column('facebook_link', sa.VARCHAR(length=240), autoincrement=False, nullable=True),
    sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('seeking', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('seeking_comment', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='venues_pkey')
    )
    op.create_table('artists',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=False),
    sa.Column('website_link', sa.VARCHAR(length=240), autoincrement=False, nullable=True),
    sa.Column('facebook_link', sa.VARCHAR(length=240), autoincrement=False, nullable=True),
    sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('seeking', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('seeking_comment', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='artists_pkey')
    )
    op.drop_table('venue')
    op.drop_table('artist')
    # ### end Alembic commands ###
