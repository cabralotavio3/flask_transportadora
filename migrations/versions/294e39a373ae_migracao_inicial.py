"""Migracao inicial

Revision ID: 294e39a373ae
Revises: bc87afd98378
Create Date: 2024-09-06 13:45:35.415091

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '294e39a373ae'
down_revision = 'bc87afd98378'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Transportadoras',
    sa.Column('id_transportadora', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('contato', sa.String(length=100), nullable=True),
    sa.Column('regiao_atuacao', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id_transportadora')
    )
    op.drop_table('usuario')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nome', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('idade', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('Transportadoras')
    # ### end Alembic commands ###
