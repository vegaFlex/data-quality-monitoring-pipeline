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

## Setup

1. Create a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Copy `.env.example` to `.env`.
4. Fill in your PostgreSQL credentials.
5. Run `python run_pipeline.py`.
