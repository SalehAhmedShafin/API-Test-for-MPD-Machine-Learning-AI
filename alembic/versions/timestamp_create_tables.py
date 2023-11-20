from alembic import op
import sqlalchemy as sa

revision = '20231120_113000'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'authors',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('full_name', sa.String, index=True),
    )

    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, index=True),
        sa.Column('author_id', sa.Integer, sa.ForeignKey('authors.id')),
    )

    op.create_table(
        'clients',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('full_name', sa.String),
    )

def downgrade():
    op.drop_table('clients')
    op.drop_table('books')
    op.drop_table('authors')
