import pandas as pd


KEY_COLUMNS = [
    "order_id",
    "customer_id",
]


def run_key_checks(dataframe: pd.DataFrame) -> list[dict]:
    results = []

    for column_name in KEY_COLUMNS:
        missing_key_count = int(dataframe[column_name].isna().sum())
        results.append(
            {
                "check_name": "key_check",
                "column_name": column_name,
                "issue_count": missing_key_count,
                "status": "PASS" if missing_key_count == 0 else "FAIL",
            }
        )

    return results


def print_key_check_results(results: list[dict]) -> None:
    print("Key check results:")
    for result in results:
        print(
            f"- {result['column_name']}: "
            f"status={result['status']}, issue_count={result['issue_count']}"
        )
