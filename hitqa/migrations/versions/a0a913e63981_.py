"""empty message

Revision ID: a0a913e63981
Revises: c72780b7a096
Create Date: 2017-08-15 22:25:14.967000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a0a913e63981'
down_revision = 'c72780b7a096'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'content',
               existing_type=mysql.TEXT(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'content',
               existing_type=mysql.TEXT(),
               nullable=False)
    # ### end Alembic commands ###
