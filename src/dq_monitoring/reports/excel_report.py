from pathlib import Path

import pandas as pd


REPORTS_DIR = Path("reports")


def generate_excel_report(results: list[dict], run_id: str) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_DIR / f"data_quality_report_{run_id}.xlsx"

    report_dataframe = pd.DataFrame(results)
    report_dataframe.insert(0, "run_id", run_id)

    with pd.ExcelWriter(report_path, engine="openpyxl") as writer:
        report_dataframe.to_excel(writer, sheet_name="quality_results", index=False)

    return report_path


def print_report_summary(report_path: Path) -> None:
    print(f"Excel report created: {report_path}")
