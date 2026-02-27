
ALTER TABLE fact_transactions
CLUSTER BY (customer_id, txn_date);




SELECT *
FROM fact_transactions
WHERE txn_date >= CURRENT_DATE - 7;

ALTER TABLE fact_transactions
SET DATA_RETENTION_TIME_IN_DAYS = 7;


ALTER TABLE fact_transactions
CLUSTER BY (customer_id, time_id);