
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from app import models
from app.database import DATABASE_URL


config = context.config
fileConfig(config.config_file_name)
config.set_main_option('sqlalchemy.url', DATABASE_URL)

sqlalchemy_engine = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix='sqlalchemy.',
    poolclass=pool.NullPool)

config.attributes['engine'] = sqlalchemy_engine

target_metadata = models.Base.metadata
