"""Initial migration.

Revision ID: 28c07f53f108
Revises: 
Create Date: 2020-07-08 04:30:18.364031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28c07f53f108'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('county', sa.String(), nullable=False),
    sa.Column('postal_code', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('catalog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tea_category', sa.String(), nullable=False),
    sa.Column('tea_packing', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clients',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('county', sa.String(), nullable=False),
    sa.Column('postal_code', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('discount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('company_contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('requisites', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('tea',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('short_title', sa.String(), nullable=False),
    sa.Column('long_title', sa.String(), nullable=True),
    sa.Column('tea_type', sa.String(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('packaging', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('ingredients', sa.String(), nullable=False),
    sa.Column('instruction', sa.String(), nullable=True),
    sa.Column('tea_quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('long_title'),
    sa.UniqueConstraint('short_title')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tea_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('total_price', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('delivered_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['tea_id'], ['tea.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tea_catalog',
    sa.Column('catalog_id', sa.Integer(), nullable=False),
    sa.Column('tea_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['catalog_id'], ['catalog.id'], ),
    sa.ForeignKeyConstraint(['tea_id'], ['tea.id'], ),
    sa.PrimaryKeyConstraint('catalog_id', 'tea_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tea_catalog')
    op.drop_table('orders')
    op.drop_table('tea')
    op.drop_table('company_contacts')
    op.drop_table('clients')
    op.drop_table('catalog')
    op.drop_table('admins')
    # ### end Alembic commands ###