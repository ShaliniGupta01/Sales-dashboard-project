from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "API running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/revenue")
def revenue():
    return {
        "status": "success",
        "rows": 4,
        "data": [
            {"order_year_month": "2023-01", "revenue": 500},
            {"order_year_month": "2023-02", "revenue": 900},
            {"order_year_month": "2023-03", "revenue": 300},
            {"order_year_month": "2023-04", "revenue": 450},
        ],
    }


@app.get("/api/top-customers")
def top_customers():
    return {
        "status": "success",
        "rows": 3,
        "data": [
            {"customer_id": 1, "name": "John Doe", "region": "North", "total_spend": 500},
            {"customer_id": 2, "name": "Alice Smith", "region": "South", "total_spend": 900},
            {"customer_id": 3, "name": "Bob Brown", "region": "East", "total_spend": 300},
        ],
    }


@app.get("/api/categories")
def categories():
    return {
        "status": "success",
        "rows": 1,
        "data": [
            {
                "category": "Electronics",
                "total_revenue": 1700,
                "avg_order_value": 566.67,
                "orders": 3,
            }
        ],
    }


@app.get("/api/regions")
def regions():
    return {
        "status": "success",
        "rows": 5,
        "data": [
            {
                "region": "North",
                "customers": 20,
                "orders": 45,
                "total_revenue": 12000,
                "avg_revenue_per_customer": 600,
            },
            {
                "region": "South",
                "customers": 15,
                "orders": 30,
                "total_revenue": 8500,
                "avg_revenue_per_customer": 566,
            },
            {
                "region": "East",
                "customers": 18,
                "orders": 35,
                "total_revenue": 9200,
                "avg_revenue_per_customer": 511,
            },
            {
                "region": "West",
                "customers": 12,
                "orders": 25,
                "total_revenue": 7000,
                "avg_revenue_per_customer": 583,
            },
            {
                "region": "Unknown",
                "customers": 5,
                "orders": 10,
                "total_revenue": 2000,
                "avg_revenue_per_customer": 400,
            },
        ],
    }