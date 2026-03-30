from src.dq_monitoring.checks.null_checks import (
    print_null_check_results,
    run_null_checks,
)
from src.dq_monitoring.db.connection import test_connection
from src.dq_monitoring.db.reader import read_source_data, test_read_source_data


if __name__ == "__main__":
    test_connection()
    test_read_source_data()
    source_data = read_source_data()
    null_check_results = run_null_checks(source_data)
    print_null_check_results(null_check_results)
