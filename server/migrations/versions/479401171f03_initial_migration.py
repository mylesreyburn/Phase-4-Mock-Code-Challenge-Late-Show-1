"""Initial migration.

Revision ID: 479401171f03
Revises: 5de24ecc04c8
Create Date: 2023-04-12 12:14:13.004297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '479401171f03'
down_revision = '5de24ecc04c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appearances', schema=None) as batch_op:
        batch_op.add_column(sa.Column('episode_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('guest_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_appearances_episode_id_episodes'), 'episodes', ['episode_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_appearances_guest_id_guests'), 'guests', ['guest_id'], ['id'])

    with op.batch_alter_table('episodes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('number', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    with op.batch_alter_table('guests', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('occupation', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guests', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('occupation')
        batch_op.drop_column('name')

    with op.batch_alter_table('episodes', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('number')
        batch_op.drop_column('date')

    with op.batch_alter_table('appearances', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_appearances_guest_id_guests'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_appearances_episode_id_episodes'), type_='foreignkey')
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('rating')
        batch_op.drop_column('guest_id')
        batch_op.drop_column('episode_id')

    # ### end Alembic commands ###
