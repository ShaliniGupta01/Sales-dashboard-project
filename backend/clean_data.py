import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
OUT = Path("data/processed")

OUT.mkdir(parents=True, exist_ok=True)

def parse_date(val):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"):
        try:
            return pd.to_datetime(val, format=fmt)
        except:
            continue
    return pd.NaT


def clean_customers():

    df = pd.read_csv(RAW / "customers.csv")

    df = df.sort_values("signup_date")
    df = df.drop_duplicates("customer_id", keep="last")

    df["email"] = df["email"].str.lower()

    df["is_valid_email"] = (
        df["email"].str.contains("@", na=False)
        & df["email"].str.contains(".", na=False)
    )

    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")

    df["name"] = df["name"].str.strip()
    df["region"] = df["region"].str.strip()

    df["region"] = df["region"].fillna("Unknown")

    df.to_csv(OUT / "customers_clean.csv", index=False)


def clean_orders():

    df = pd.read_csv(RAW / "orders.csv")

    df["order_date"] = df["order_date"].apply(parse_date)

    df = df.dropna(subset=["order_id", "customer_id"], how="all")

    df["amount"] = df.groupby("product")["amount"].transform(
        lambda x: x.fillna(x.median())
    )

    status_map = {
        "done": "completed",
        "completed": "completed",
        "pending": "pending",
        "canceled": "cancelled",
        "cancelled": "cancelled",
        "refunded": "refunded",
    }

    df["status"] = df["status"].str.lower().map(status_map)

    df["order_year_month"] = df["order_date"].dt.strftime("%Y-%m")

    df.to_csv(OUT / "orders_clean.csv", index=False)


if __name__ == "__main__":
    clean_customers()
    clean_orders()

print("Cleaning Complete")