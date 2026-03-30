# Data Quality Monitoring Pipeline

Production-style portfolio project for automated data quality monitoring with PostgreSQL, pandas, SQLAlchemy, Excel reporting, email alerts, logging, scheduler support, and Power BI-ready views.

## Features

- Reads source data from PostgreSQL
- Runs automated data quality checks
- Writes results into `dq_monitoring.data_quality_log`
- Generates Excel quality reports in `reports/`
- Writes execution logs to `logs/pipeline.log`
- Supports email alerts
- Supports Windows Task Scheduler execution
- Exposes Power BI-ready SQL views

## Tech Stack

- Python
- PostgreSQL
- pandas
- SQLAlchemy
- openpyxl
- smtplib
- logging
- Power BI

## Checks Implemented

- NULL checks
- Duplicate checks
- Negative value checks
- Date checks
- Key checks
- Type checks

## Project Structure

- `run_pipeline.py` - entry point
- `run_pipeline.bat` - scheduler entry point for Windows
- `config/db_config.py` - environment-based configuration
- `src/dq_monitoring/db/` - database connection, reading, and logging
- `src/dq_monitoring/checks/` - data quality check modules
- `src/dq_monitoring/reports/` - Excel report generation
- `src/dq_monitoring/alerts/` - email alert logic
- `src/dq_monitoring/logging_config/` - logger setup
- `src/dq_monitoring/pipeline/runner.py` - pipeline orchestration
- `sql/` - table setup, seed data, and Power BI views

## Setup

1. Create a virtual environment
2. Install dependencies from `requirements.txt`
3. Copy `.env.example` to `.env`
4. Fill in your PostgreSQL and optional email settings
5. Run `python run_pipeline.py`

## SQL Setup

- `sql/create_source_tables.sql`
- `sql/create_data_quality_log.sql`
- `sql/seed_source_data.sql`
- `sql/create_power_bi_views.sql`

## Outputs

- Log table: `dq_monitoring.data_quality_log`
- Excel reports: `reports/data_quality_report_<run_id>.xlsx`
- Log file: `logs/pipeline.log`
- Power BI views:
  - `dq_monitoring.vw_quality_status`
  - `dq_monitoring.vw_quality_summary`

## Email Alerts

- Email alerts are controlled by `EMAIL_ALERT_ENABLED`
- Default in `.env.example` is `false`
- This keeps the project safe until real SMTP credentials are added

## Scheduler

For Windows Task Scheduler:

1. Open Task Scheduler
2. Create a new Basic Task
3. Choose your trigger
4. Set the action to:
   `C:\Users\vega_\Documents\Playground\data-quality-monitoring-pipeline\run_pipeline.bat`

## Power BI

Recommended visuals:

- Card: total failed checks
- Card: total issues
- Clustered bar chart: issues by check name
- Table: failed checks by column
- Slicer: `run_id`
