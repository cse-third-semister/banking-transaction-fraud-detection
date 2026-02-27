import pandas as pd

def transform_transactions(txn_df):
    
    
    txn_df["is_fraud"] = txn_df["amount"] > 200000
    txn_df["fraud_score"] = (txn_df["amount"] / 1000).astype(int)

    txn_df["device_info"] = txn_df.apply(
        lambda x: {
            "channel": x["channel"],
            "risk": "HIGH" if x["is_fraud"] else "LOW"
        },
        axis=1
    )

    return txn_df


def transform_customers(cust_df):
    return cust_df.drop_duplicates("customer_id")


def transform_merchants(merch_df):
    return merch_df.drop_duplicates("merchant_id")