import pandas as pd
from pandas.api.types import is_datetime64_any_dtype, is_numeric_dtype


def run_type_checks(dataframe: pd.DataFrame) -> list[dict]:
    results = [
        build_type_result(
            column_name="quantity",
            issue_count=0 if is_numeric_dtype(dataframe["quantity"]) else 1,
        ),
        build_type_result(
            column_name="unit_price",
            issue_count=0 if is_numeric_dtype(dataframe["unit_price"]) else 1,
        ),
        build_type_result(
            column_name="order_date",
            issue_count=0 if is_datetime64_any_dtype(dataframe["order_date"]) else 1,
        ),
        build_type_result(
            column_name="shipment_date",
            issue_count=(
                0 if is_datetime64_any_dtype(dataframe["shipment_date"]) else 1
            ),
        ),
    ]

    return results


def build_type_result(column_name: str, issue_count: int) -> dict:
    return {
        "check_name": "type_check",
        "column_name": column_name,
        "issue_count": issue_count,
        "status": "PASS" if issue_count == 0 else "FAIL",
    }


def print_type_check_results(results: list[dict]) -> None:
    print("Type check results:")
    for result in results:
        print(
            f"- {result['column_name']}: "
            f"status={result['status']}, issue_count={result['issue_count']}"
        )
