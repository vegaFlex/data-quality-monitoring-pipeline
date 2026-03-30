import pandas as pd

from src.dq_monitoring.db.connection import get_engine


SOURCE_TABLE_NAME = "dq_monitoring.customer_orders_source"
DATE_COLUMNS = ["order_date", "shipment_date", "created_at"]


def read_source_data() -> pd.DataFrame:
    engine = get_engine()
    query = f"SELECT * FROM {SOURCE_TABLE_NAME} ORDER BY row_id;"
    return pd.read_sql(query, engine, parse_dates=DATE_COLUMNS)


def test_read_source_data() -> None:
    dataframe = read_source_data()
    print(f"Rows loaded: {len(dataframe)}")
    print("Columns loaded:", list(dataframe.columns))
    print(dataframe.head())
