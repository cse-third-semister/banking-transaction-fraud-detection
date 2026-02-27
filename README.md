Bank Fraud Detection System
📌 Abstract

The Bank Fraud Detection System is an end-to-end data engineering and analytics project designed to detect potentially fraudulent banking transactions using rule-based detection logic and big data processing techniques.

The system integrates ETL processing, Spark-based batch/stream analysis, and an interactive Streamlit dashboard for real-time visualization of fraud insights.

🎯 Objectives

Detect high-risk transactions based on transaction amount.

Process banking data using ETL pipeline.

Perform batch and streaming fraud analysis using Apache Spark.

Visualize fraud insights using Streamlit dashboard.

Demonstrate real-world data engineering workflow.

🏗️ System Architecture
Raw CSV Data
      ↓
ETL Pipeline (Python)
      ↓
Snowflake Data Warehouse (Optional)
      ↓
Spark Batch / Streaming Processing
      ↓
Streamlit Dashboard Visualization
📂 Project Structure
Bank-Fraud-Detection-System/
│
├── data/
│   └── raw/
│       └── transactions.csv
│
├── etl/
│   └── load_to_snowflake.py
│
├── spark/
│   ├── batch_fraud_analysis.py
│   └── streaming_fraud_detection.py
│
├── dashboard/
│   └── dashboard.py
│
├── requirements.txt
└── README.md
⚙️ Tech Stack
Layer	Technology
Programming	Python
Data Processing	Pandas
Big Data	Apache Spark
Data Warehouse	Snowflake
Visualization	Streamlit
Environment	Virtual Environment (venv)
🔎 Fraud Detection Logic

Currently, fraud detection uses rule-based logic:

is_fraud = amount > 200000

Transactions exceeding ₹200,000 are classified as fraudulent.

This logic can be extended using:

Machine Learning models

Anomaly detection

Behavioral analysis

🚀 How to Run the Project
1️⃣ Create Virtual Environment
python -m venv venv
2️⃣ Activate Environment

PowerShell

.\venv\Scripts\Activate.ps1

Command Prompt

venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run ETL Pipeline (Optional – Snowflake Integration)
python -m etl.load_to_snowflake
5️⃣ Run Spark Batch Processing
spark-submit spark/batch_fraud_analysis.py
6️⃣ Run Streamlit Dashboard
streamlit run dashboard/dashboard.py

Open browser:

http://localhost:8501
📊 Dashboard Features

Total Transactions Overview

Fraud Transaction Count

Fraud Percentage

Fraud Distribution by Channel

Complete Transaction Data Table

Interactive Visualization

📈 Future Enhancements

Machine Learning fraud prediction model

Real-time Kafka integration

Role-based authentication

Cloud deployment (AWS / Azure)

Advanced anomaly detection algorithms

