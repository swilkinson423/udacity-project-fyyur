"""empty message

Revision ID: 865f77265ea5
Revises: 98f7726eda35
Create Date: 2023-02-06 19:04:22.948130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '865f77265ea5'
down_revision = '98f7726eda35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website_link', sa.String(length=240), nullable=True))
        batch_op.add_column(sa.Column('seeking', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('seeking_comment', sa.String(length=500), nullable=True))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('facebook_link',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=240),
               existing_nullable=True)
        batch_op.alter_column('genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website_link', sa.String(length=240), nullable=True))
        batch_op.add_column(sa.Column('genres', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('seeking', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('seeking_comment', sa.String(length=500), nullable=True))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('facebook_link',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=240),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.alter_column('facebook_link',
               existing_type=sa.String(length=240),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)
        batch_op.alter_column('image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('seeking_comment')
        batch_op.drop_column('seeking')
        batch_op.drop_column('genres')
        batch_op.drop_column('website_link')

    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.alter_column('genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('facebook_link',
               existing_type=sa.String(length=240),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)
        batch_op.alter_column('image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('seeking_comment')
        batch_op.drop_column('seeking')
        batch_op.drop_column('website_link')

    op.drop_table('shows')
    # ### end Alembic commands ###
