import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Bank Trsanction Fraud Dashboard", layout="wide")

st.title("🏦 Banking Transaction Fraud Detection Dashboard")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "transactions.csv")

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()


df["is_fraud"] = df["amount"] > 200000


col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", len(df))
col2.metric("Fraud Transactions", int(df["is_fraud"].sum()))
col3.metric(
    "Fraud %",
    f"{round((df['is_fraud'].sum() / len(df)) * 100, 2)}%"
)

st.divider()


st.subheader("Fraud by Channel")
fraud_by_channel = (
    df.groupby("channel")["is_fraud"]
      .sum()
      .reset_index()
)
st.bar_chart(fraud_by_channel, x="channel", y="is_fraud")


st.subheader("Transaction Details")
st.dataframe(df)