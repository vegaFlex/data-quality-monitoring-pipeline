CREATE SCHEMA IF NOT EXISTS dq_monitoring;

CREATE OR REPLACE VIEW dq_monitoring.vw_quality_status AS
SELECT
    run_id,
    check_name,
    check_status,
    table_name,
    column_name,
    issue_count,
    issue_details,
    detected_at
FROM dq_monitoring.data_quality_log;

CREATE OR REPLACE VIEW dq_monitoring.vw_quality_summary AS
SELECT
    run_id,
    check_name,
    COUNT(*) AS total_checks,
    SUM(CASE WHEN check_status = 'FAIL' THEN 1 ELSE 0 END) AS failed_checks,
    SUM(issue_count) AS total_issues,
    MAX(detected_at) AS detected_at
FROM dq_monitoring.data_quality_log
GROUP BY run_id, check_name;
