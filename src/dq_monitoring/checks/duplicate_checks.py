import pandas as pd


DUPLICATE_KEY_COLUMNS = [
    "order_id",
    "customer_id",
    "product_name",
    "order_date",
]


def run_duplicate_checks(dataframe: pd.DataFrame) -> list[dict]:
    duplicate_mask = dataframe.duplicated(subset=DUPLICATE_KEY_COLUMNS, keep=False)
    duplicate_count = int(duplicate_mask.sum())

    return [
        {
            "check_name": "duplicate_check",
            "column_name": ",".join(DUPLICATE_KEY_COLUMNS),
            "issue_count": duplicate_count,
            "status": "PASS" if duplicate_count == 0 else "FAIL",
        }
    ]


def print_duplicate_check_results(results: list[dict]) -> None:
    print("Duplicate check results:")
    for result in results:
        print(
            f"- {result['column_name']}: "
            f"status={result['status']}, issue_count={result['issue_count']}"
        )
