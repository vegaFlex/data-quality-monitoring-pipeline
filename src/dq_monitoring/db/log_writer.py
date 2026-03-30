from sqlalchemy import text

from src.dq_monitoring.db.connection import get_engine


LOG_TABLE_NAME = "dq_monitoring.data_quality_log"
SOURCE_TABLE_NAME = "dq_monitoring.customer_orders_source"


def write_check_results_to_log(results: list[dict], run_id: str) -> None:
    engine = get_engine()

    insert_statement = text(
        f"""
        INSERT INTO {LOG_TABLE_NAME} (
            run_id,
            check_name,
            check_status,
            table_name,
            column_name,
            issue_count,
            issue_details
        )
        VALUES (
            :run_id,
            :check_name,
            :check_status,
            :table_name,
            :column_name,
            :issue_count,
            :issue_details
        );
        """
    )

    rows_to_insert = []
    for result in results:
        issue_details = build_issue_details(result)
        rows_to_insert.append(
            {
                "run_id": run_id,
                "check_name": result["check_name"],
                "check_status": result["status"],
                "table_name": SOURCE_TABLE_NAME,
                "column_name": result["column_name"],
                "issue_count": result["issue_count"],
                "issue_details": issue_details,
            }
        )

    with engine.begin() as connection:
        connection.execute(insert_statement, rows_to_insert)


def print_log_write_summary(results: list[dict], run_id: str) -> None:
    print(
        f"Inserted {len(results)} log rows into {LOG_TABLE_NAME} "
        f"for run_id={run_id}"
    )


def build_issue_details(result: dict) -> str:
    if result["check_name"] == "null_check":
        return (
            f"NULL values found in column {result['column_name']}"
            if result["issue_count"] > 0
            else "No NULL values found"
        )

    if result["check_name"] == "duplicate_check":
        return (
            f"Duplicate records found for key {result['column_name']}"
            if result["issue_count"] > 0
            else "No duplicate records found"
        )

    if result["check_name"] == "negative_value_check":
        return (
            f"Negative values found in column {result['column_name']}"
            if result["issue_count"] > 0
            else "No negative values found"
        )

    if result["check_name"] == "date_check":
        if result["column_name"] == "shipment_date":
            return (
                "Missing shipment dates found"
                if result["issue_count"] > 0
                else "No missing shipment dates found"
            )

        return (
            "Shipment date is earlier than order date"
            if result["issue_count"] > 0
            else "Date order is valid"
        )

    if result["check_name"] == "key_check":
        return (
            f"Missing key values found in column {result['column_name']}"
            if result["issue_count"] > 0
            else "No missing key values found"
        )

    return "Check completed"
