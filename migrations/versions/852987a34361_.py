"""empty message

Revision ID: 852987a34361
Revises: 75dad4233215
Create Date: 2022-05-28 21:01:46.356901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '852987a34361'
down_revision = '75dad4233215'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planets', sa.Column('diameter', sa.String(length=120), nullable=False))
    op.add_column('planets', sa.Column('rotation_period', sa.String(length=120), nullable=False))
    op.add_column('planets', sa.Column('orbital_period', sa.String(length=120), nullable=False))
    op.add_column('planets', sa.Column('gravity', sa.String(length=120), nullable=False))
    op.add_column('planets', sa.Column('population', sa.String(length=120), nullable=False))
    op.add_column('planets', sa.Column('climate', sa.String(length=120), nullable=False))
    op.add_column('planets', sa.Column('terrain', sa.String(length=120), nullable=False))
    op.add_column('planets', sa.Column('surface_water', sa.String(length=120), nullable=False))
    op.add_column('planets', sa.Column('created', sa.String(length=120), nullable=False))
    op.add_column('planets', sa.Column('edited', sa.String(length=120), nullable=False))
    op.add_column('planets', sa.Column('name', sa.String(length=120), nullable=False))
    op.add_column('planets', sa.Column('url', sa.String(length=120), nullable=False))
    op.add_column('planets', sa.Column('description', sa.String(length=120), nullable=True))
    op.add_column('planets', sa.Column('_id', sa.String(length=120), nullable=True))
    op.add_column('planets', sa.Column('uid', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planets', 'uid')
    op.drop_column('planets', '_id')
    op.drop_column('planets', 'description')
    op.drop_column('planets', 'url')
    op.drop_column('planets', 'name')
    op.drop_column('planets', 'edited')
    op.drop_column('planets', 'created')
    op.drop_column('planets', 'surface_water')
    op.drop_column('planets', 'terrain')
    op.drop_column('planets', 'climate')
    op.drop_column('planets', 'population')
    op.drop_column('planets', 'gravity')
    op.drop_column('planets', 'orbital_period')
    op.drop_column('planets', 'rotation_period')
    op.drop_column('planets', 'diameter')
    # ### end Alembic commands ###