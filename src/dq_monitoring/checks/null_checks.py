import pandas as pd


REQUIRED_COLUMNS = [
    "order_id",
    "customer_id",
    "customer_email",
    "product_name",
    "quantity",
    "unit_price",
    "order_date",
]


def run_null_checks(dataframe: pd.DataFrame) -> list[dict]:
    results = []

    for column_name in REQUIRED_COLUMNS:
        null_count = int(dataframe[column_name].isna().sum())
        results.append(
            {
                "check_name": "null_check",
                "column_name": column_name,
                "issue_count": null_count,
                "status": "PASS" if null_count == 0 else "FAIL",
            }
        )

    return results


def print_null_check_results(results: list[dict]) -> None:
    print("NULL check results:")
    for result in results:
        print(
            f"- {result['column_name']}: "
            f"status={result['status']}, issue_count={result['issue_count']}"
        )
