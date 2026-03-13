import pandas as pd
from pathlib import Path

DATA = Path("data")
OUT = DATA / "processed"

customers = pd.read_csv(OUT / "customers_clean.csv")
orders = pd.read_csv(OUT / "orders_clean.csv")
products = pd.read_csv(DATA / "raw/products.csv")

orders_with_customers = pd.merge(
    orders, customers, on="customer_id", how="left"
)

full_data = pd.merge(
    orders_with_customers,
    products,
    left_on="product",
    right_on="product_name",
    how="left",
)

completed = full_data[full_data["status"] == "completed"]

monthly = completed.groupby("order_year_month")["amount"].sum().reset_index()
monthly.columns = ["order_year_month", "revenue"]

monthly.to_csv(OUT / "monthly_revenue.csv", index=False)

top = (
    completed.groupby(["customer_id", "name", "region"])["amount"]
    .sum()
    .reset_index()
)

top = top.sort_values("amount", ascending=False).head(10)
top.columns = ["customer_id", "name", "region", "total_spend"]

top.to_csv(OUT / "top_customers.csv", index=False)

category = (
    completed.groupby("category")
    .agg(
        total_revenue=("amount", "sum"),
        avg_order_value=("amount", "mean"),
        orders=("order_id", "count"),
    )
    .reset_index()
)

category.to_csv(OUT / "category_performance.csv", index=False)

region = (
    full_data.groupby("region")
    .agg(
        customers=("customer_id", "nunique"),
        orders=("order_id", "count"),
        total_revenue=("amount", "sum"),
    )
    .reset_index()
)

region["avg_revenue_per_customer"] = (
    region["total_revenue"] / region["customers"]
)

region.to_csv(OUT / "regional_analysis.csv", index=False)

print("Analysis Complete")