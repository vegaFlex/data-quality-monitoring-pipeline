from datetime import datetime

from src.dq_monitoring.checks.date_checks import (
    print_date_check_results,
    run_date_checks,
)
from src.dq_monitoring.checks.duplicate_checks import (
    print_duplicate_check_results,
    run_duplicate_checks,
)
from src.dq_monitoring.checks.negative_value_checks import (
    print_negative_value_check_results,
    run_negative_value_checks,
)
from src.dq_monitoring.checks.null_checks import (
    print_null_check_results,
    run_null_checks,
)
from src.dq_monitoring.db.connection import test_connection
from src.dq_monitoring.db.log_writer import (
    print_log_write_summary,
    write_check_results_to_log,
)
from src.dq_monitoring.db.reader import read_source_data, test_read_source_data


if __name__ == "__main__":
    run_id = datetime.now().strftime("%Y%m%d%H%M%S")
    test_connection()
    test_read_source_data()
    source_data = read_source_data()
    null_check_results = run_null_checks(source_data)
    date_check_results = run_date_checks(source_data)
    duplicate_check_results = run_duplicate_checks(source_data)
    negative_value_check_results = run_negative_value_checks(source_data)
    all_check_results = (
        null_check_results
        + date_check_results
        + duplicate_check_results
        + negative_value_check_results
    )
    print_null_check_results(null_check_results)
    print_date_check_results(date_check_results)
    print_duplicate_check_results(duplicate_check_results)
    print_negative_value_check_results(negative_value_check_results)
    write_check_results_to_log(all_check_results, run_id)
    print_log_write_summary(all_check_results, run_id)
