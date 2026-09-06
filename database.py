import sqlite3
import pandas as pd


# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv("Data/customer_churn.csv")


# ============================================================
# CREATE DATABASE
# ============================================================

conn = sqlite3.connect("customer_churn.db")


df.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)


print("Database created successfully!")


# ============================================================
# SQL QUERY 1 - TOTAL CUSTOMERS
# ============================================================

query = """
SELECT COUNT(*) AS total_customers
FROM customers;
"""

print("\nTOTAL CUSTOMERS")
print(pd.read_sql_query(query, conn))


# ============================================================
# SQL QUERY 2 - CHURN DISTRIBUTION
# ============================================================

query = """
SELECT
    Churn,
    COUNT(*) AS customers
FROM customers
GROUP BY Churn;
"""

print("\nCHURN DISTRIBUTION")
print(pd.read_sql_query(query, conn))


# ============================================================
# SQL QUERY 3 - CHURN RATE BY CONTRACT
# ============================================================

query = """
SELECT
    Contract,
    COUNT(*) AS total_customers,

    SUM(
        CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END
    ) AS churned_customers,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY Contract

ORDER BY churn_rate DESC;
"""

print("\nCHURN RATE BY CONTRACT")
print(pd.read_sql_query(query, conn))


# ============================================================
# SQL QUERY 4 - CHURN RATE BY INTERNET SERVICE
# ============================================================

query = """
SELECT
    InternetService,
    COUNT(*) AS total_customers,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY InternetService

ORDER BY churn_rate DESC;
"""

print("\nCHURN RATE BY INTERNET SERVICE")
print(pd.read_sql_query(query, conn))


# ============================================================
# SQL QUERY 5 - CHURN RATE BY PAYMENT METHOD
# ============================================================

query = """
SELECT
    PaymentMethod,
    COUNT(*) AS total_customers,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS churn_rate

FROM customers

GROUP BY PaymentMethod

ORDER BY churn_rate DESC;
"""

print("\nCHURN RATE BY PAYMENT METHOD")
print(pd.read_sql_query(query, conn))


# ============================================================
# SQL QUERY 6 - AVG MONTHLY CHARGES BY CHURN
# ============================================================

query = """
SELECT
    Churn,

    ROUND(
        AVG(MonthlyCharges),
        2
    ) AS avg_monthly_charges

FROM customers

GROUP BY Churn;
"""

print("\nAVERAGE MONTHLY CHARGES BY CHURN")
print(pd.read_sql_query(query, conn))


# ============================================================
# CLOSE DATABASE
# ============================================================

conn.close()


print("\nSQL ANALYSIS COMPLETED SUCCESSFULLY!")