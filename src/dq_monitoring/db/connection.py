from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError

from config.db_config import DBConfig


def get_engine() -> Engine:
    connection_url = DBConfig.get_connection_url()
    return create_engine(connection_url, pool_pre_ping=True)


def test_connection() -> None:
    try:
        engine = get_engine()
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1 AS connection_test;"))
            row = result.fetchone()
            print(f"PostgreSQL connection successful: {row[0]}")
    except SQLAlchemyError as exc:
        raise RuntimeError(f"Database connection failed: {exc}") from exc
