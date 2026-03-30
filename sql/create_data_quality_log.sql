CREATE SCHEMA IF NOT EXISTS dq_monitoring;

CREATE TABLE IF NOT EXISTS dq_monitoring.data_quality_log (
    log_id BIGSERIAL PRIMARY KEY,
    run_id VARCHAR(50) NOT NULL,
    check_name VARCHAR(100) NOT NULL,
    check_status VARCHAR(20) NOT NULL,
    table_name VARCHAR(150) NOT NULL,
    column_name VARCHAR(150),
    issue_count INTEGER NOT NULL DEFAULT 0,
    issue_details TEXT,
    detected_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
