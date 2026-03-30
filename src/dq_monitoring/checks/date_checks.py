import pandas as pd


def run_date_checks(dataframe: pd.DataFrame) -> list[dict]:
    missing_shipment_date_count = int(dataframe["shipment_date"].isna().sum())
    invalid_date_order_count = int(
        (
            dataframe["order_date"].notna()
            & dataframe["shipment_date"].notna()
            & (dataframe["shipment_date"] < dataframe["order_date"])
        ).sum()
    )

    return [
        {
            "check_name": "date_check",
            "column_name": "shipment_date",
            "issue_count": missing_shipment_date_count,
            "status": "PASS" if missing_shipment_date_count == 0 else "FAIL",
        },
        {
            "check_name": "date_check",
            "column_name": "order_date,shipment_date",
            "issue_count": invalid_date_order_count,
            "status": "PASS" if invalid_date_order_count == 0 else "FAIL",
        },
    ]


def print_date_check_results(results: list[dict]) -> None:
    print("Date check results:")
    for result in results:
        print(
            f"- {result['column_name']}: "
            f"status={result['status']}, issue_count={result['issue_count']}"
        )
