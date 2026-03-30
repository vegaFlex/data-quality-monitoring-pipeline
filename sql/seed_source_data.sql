TRUNCATE TABLE dq_monitoring.customer_orders_source RESTART IDENTITY;

INSERT INTO dq_monitoring.customer_orders_source (
    order_id,
    customer_id,
    customer_email,
    product_name,
    quantity,
    unit_price,
    order_date,
    shipment_date,
    source_file_name
)
VALUES
    (1001, 501, 'anna@example.com', 'Laptop Stand', 2, 45.50, DATE '2026-03-10', DATE '2026-03-12', 'orders_batch_01.xlsx'),
    (1002, 502, 'boris@example.com', 'Wireless Mouse', 1, 25.00, DATE '2026-03-11', DATE '2026-03-13', 'orders_batch_01.xlsx'),
    (1003, NULL, 'mira@example.com', 'Keyboard', 1, 55.00, DATE '2026-03-12', DATE '2026-03-14', 'orders_batch_01.xlsx'),
    (1004, 504, NULL, 'Monitor', 1, 199.99, DATE '2026-03-13', DATE '2026-03-15', 'orders_batch_01.xlsx'),
    (1004, 504, NULL, 'Monitor', 1, 199.99, DATE '2026-03-13', DATE '2026-03-15', 'orders_batch_01.xlsx'),
    (1005, 505, 'ivan@example.com', 'Docking Station', -1, 120.00, DATE '2026-03-14', DATE '2026-03-16', 'orders_batch_02.xlsx'),
    (1006, 506, 'elena@example.com', 'Headset', 1, -35.00, DATE '2026-03-15', DATE '2026-03-17', 'orders_batch_02.xlsx'),
    (1007, 507, 'petar@example.com', 'Webcam', 1, 89.99, DATE '2026-04-20', DATE '2026-04-18', 'orders_batch_02.xlsx'),
    (NULL, 508, 'stela@example.com', 'USB Hub', 3, 15.00, DATE '2026-03-18', DATE '2026-03-20', 'orders_batch_02.xlsx'),
    (1008, 509, 'nina@example.com', 'Office Chair', 1, 310.00, NULL, DATE '2026-03-22', 'orders_batch_03.xlsx');
