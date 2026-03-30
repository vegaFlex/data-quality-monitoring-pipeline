import pandas as pd


NON_NEGATIVE_COLUMNS = [
    "quantity",
    "unit_price",
]


def run_negative_value_checks(dataframe: pd.DataFrame) -> list[dict]:
    results = []

    for column_name in NON_NEGATIVE_COLUMNS:
        negative_count = int((dataframe[column_name] < 0).sum())
        results.append(
            {
                "check_name": "negative_value_check",
                "column_name": column_name,
                "issue_count": negative_count,
                "status": "PASS" if negative_count == 0 else "FAIL",
            }
        )

    return results


def print_negative_value_check_results(results: list[dict]) -> None:
    print("Negative value check results:")
    for result in results:
        print(
            f"- {result['column_name']}: "
            f"status={result['status']}, issue_count={result['issue_count']}"
        )
