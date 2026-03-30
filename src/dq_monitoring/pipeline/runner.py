from datetime import datetime

from src.dq_monitoring.alerts.email_alert import send_email_alert
from src.dq_monitoring.checks.date_checks import (
    print_date_check_results,
    run_date_checks,
)
from src.dq_monitoring.checks.duplicate_checks import (
    print_duplicate_check_results,
    run_duplicate_checks,
)
from src.dq_monitoring.checks.key_checks import (
    print_key_check_results,
    run_key_checks,
)
from src.dq_monitoring.checks.negative_value_checks import (
    print_negative_value_check_results,
    run_negative_value_checks,
)
from src.dq_monitoring.checks.null_checks import (
    print_null_check_results,
    run_null_checks,
)
from src.dq_monitoring.checks.type_checks import (
    print_type_check_results,
    run_type_checks,
)
from src.dq_monitoring.db.connection import test_connection
from src.dq_monitoring.db.log_writer import (
    print_log_write_summary,
    write_check_results_to_log,
)
from src.dq_monitoring.db.reader import read_source_data, test_read_source_data
from src.dq_monitoring.logging_config.logger import get_logger
from src.dq_monitoring.reports.excel_report import (
    generate_excel_report,
    print_report_summary,
)


def run_pipeline() -> None:
    logger = get_logger()
    run_id = datetime.now().strftime("%Y%m%d%H%M%S")
    logger.info("Pipeline started with run_id=%s", run_id)

    try:
        test_connection()
        test_read_source_data()
        source_data = read_source_data()

        null_check_results = run_null_checks(source_data)
        date_check_results = run_date_checks(source_data)
        duplicate_check_results = run_duplicate_checks(source_data)
        key_check_results = run_key_checks(source_data)
        negative_value_check_results = run_negative_value_checks(source_data)
        type_check_results = run_type_checks(source_data)

        all_check_results = (
            null_check_results
            + date_check_results
            + duplicate_check_results
            + key_check_results
            + negative_value_check_results
            + type_check_results
        )

        print_null_check_results(null_check_results)
        print_date_check_results(date_check_results)
        print_duplicate_check_results(duplicate_check_results)
        print_key_check_results(key_check_results)
        print_negative_value_check_results(negative_value_check_results)
        print_type_check_results(type_check_results)

        write_check_results_to_log(all_check_results, run_id)
        print_log_write_summary(all_check_results, run_id)
        report_path = generate_excel_report(all_check_results, run_id)
        print_report_summary(report_path)
        send_email_alert(all_check_results, run_id)
        logger.info(
            "Pipeline finished with run_id=%s and %s check results",
            run_id,
            len(all_check_results),
        )
    except Exception:
        logger.exception("Pipeline failed for run_id=%s", run_id)
        raise
