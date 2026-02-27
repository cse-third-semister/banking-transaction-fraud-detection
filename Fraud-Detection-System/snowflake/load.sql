
CREATE OR REPLACE FILE FORMAT fraud_csv
TYPE = 'CSV'
FIELD_OPTIONALLY_ENCLOSED_BY = '"'
SKIP_HEADER = 1;


CREATE OR REPLACE STAGE fraud_stage
FILE_FORMAT = fraud_csv;


COPY INTO dim_customer
FROM @fraud_stage/customers.csv;

COPY INTO dim_merchant
FROM @fraud_stage/merchants.csv;


COPY INTO fact_transactions
FROM @fraud_stage/transactions.csv;