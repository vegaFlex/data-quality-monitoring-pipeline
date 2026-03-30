CREATE SCHEMA IF NOT EXISTS dq_monitoring;

CREATE TABLE IF NOT EXISTS dq_monitoring.customer_orders_source (
    row_id BIGSERIAL PRIMARY KEY,
    order_id INTEGER,
    customer_id INTEGER,
    customer_email VARCHAR(255),
    product_name VARCHAR(150),
    quantity INTEGER,
    unit_price NUMERIC(10, 2),
    order_date DATE,
    shipment_date DATE,
    source_file_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
