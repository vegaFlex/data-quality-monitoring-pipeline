# Data Quality Monitoring Pipeline

Production-style portfolio project for automated data quality monitoring.

## Step 1

Current scope:
- project structure
- PostgreSQL connection setup
- connection test entry point

## Step 2

Database setup files:
- `sql/create_source_tables.sql` creates the source table in schema `dq_monitoring`
- `sql/create_data_quality_log.sql` creates the logging table in schema `dq_monitoring`
- `sql/seed_source_data.sql` inserts test data with intentional data quality issues

## Step 5

Current pipeline flow:
- test PostgreSQL connection
- read source data into pandas
- run NULL checks
- write check results into `dq_monitoring.data_quality_log`

## Current Status

- checks are orchestrated from `src/dq_monitoring/pipeline/runner.py`
- `run_pipeline.py` is now a clean entry point
- email alerts support is added with `EMAIL_ALERT_ENABLED=false` by default
- `run_pipeline.bat` is ready for Windows Task Scheduler

## Setup

1. Create a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Copy `.env.example` to `.env`.
4. Fill in your PostgreSQL credentials.
5. Run `python run_pipeline.py`.

## Scheduler

For Windows Task Scheduler:

1. Open Task Scheduler
2. Create a new Basic Task
3. Choose the trigger you want
4. Set the action to start:
   `C:\Users\vega_\Documents\Playground\data-quality-monitoring-pipeline\run_pipeline.bat`

## Power BI

Use these PostgreSQL objects in Power BI:

- `dq_monitoring.vw_quality_status`
- `dq_monitoring.vw_quality_summary`

Recommended visuals:

- Card: total failed checks
- Card: total issues
- Clustered bar chart: issues by check name
- Table: failed checks by column
- Slicer: run_id
