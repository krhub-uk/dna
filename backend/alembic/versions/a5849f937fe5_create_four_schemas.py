"""create_four_schemas

Revision ID: a5849f937fe5
Revises: 
Create Date: 2026-09-16

"""
from alembic import op

revision = 'a5849f937fe5'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.execute("CREATE SCHEMA IF NOT EXISTS dna")
    op.execute("CREATE SCHEMA IF NOT EXISTS mi")
    op.execute("CREATE SCHEMA IF NOT EXISTS logging")
    op.execute("CREATE SCHEMA IF NOT EXISTS fintiq")

def downgrade():
    op.execute("DROP SCHEMA IF EXISTS fintiq CASCADE")
    op.execute("DROP SCHEMA IF EXISTS logging CASCADE")
    op.execute("DROP SCHEMA IF EXISTS mi CASCADE")
    op.execute("DROP SCHEMA IF EXISTS dna CASCADE")
