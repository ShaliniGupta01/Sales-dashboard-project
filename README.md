# 📊 Sales Data Pipeline & Dashboard

## 📌 Project Overview

This project demonstrates an **end-to-end data pipeline and full-stack dashboard**.
The system ingests raw data, cleans and transforms it using **Python**, performs **data analysis with Pandas**, and exposes the results through a **FastAPI REST API**.
A lightweight **frontend dashboard** then consumes these APIs and displays the insights.

The goal of the project is to showcase:

* Data Cleaning
* Data Transformation
* Data Analysis
* Backend API Development
* Frontend Dashboard Visualization

---

# 🏗 Project Architecture

Raw Data → Data Cleaning → Data Analysis → API → Frontend Dashboard

```
data/raw → clean_data.py → analyze.py → data/processed → FastAPI API → Frontend Dashboard
```

---

# 📁 Project Structure

```
Assignment
│
├── backend
│   ├── main.py
│   ├── clean_data.py
│   └── analyze.py
│
├── data
│   ├── raw
│   │   ├── customers.csv
│   │   ├── orders.csv
│   │   └── products.csv
│   │
│   └── processed
│       ├── customers_clean.csv
│       ├── orders_clean.csv
│       ├── monthly_revenue.csv
│       ├── top_customers.csv
│       ├── category_performance.csv
│       └── regional_analysis.csv
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# ⚙️ Technologies Used

## Backend

* Python
* FastAPI
* Pandas

## Frontend

* HTML
* CSS
* JavaScript

## Tools

* VS Code
* Git
* Python Virtual Environment

---

# 📥 Dataset Description

The project uses three datasets:

### Customers

Contains customer information including:

* customer_id
* name
* email
* region
* signup_date

### Orders

Contains order transaction data:

* order_id
* customer_id
* product
* amount
* order_date
* status

### Products

Contains product catalog information:

* product_id
* product_name
* category
* unit_price

---

# 🧹 Data Cleaning

The **clean_data.py** script performs the following operations:

### Customers Data

* Removes duplicate customers
* Standardizes email format
* Validates email addresses
* Parses signup dates
* Handles missing regions

### Orders Data

* Standardizes order date formats
* Handles missing order amounts
* Normalizes order status values
* Creates `order_year_month` field

Output files:

```
customers_clean.csv
orders_clean.csv
```

---

# 📊 Data Analysis

The **analyze.py** script performs analysis on the cleaned data.

### Monthly Revenue

Aggregates revenue by month.

Output:

```
monthly_revenue.csv
```

---

### Top Customers

Identifies the **Top 10 customers by total spend**.

Output:

```
top_customers.csv
```

---

### Category Performance

Analyzes product categories based on:

* Total revenue
* Average order value
* Number of orders

Output:

```
category_performance.csv
```

---

### Regional Analysis

Aggregates business performance by region.

Metrics:

* Total customers
* Total orders
* Total revenue
* Average revenue per customer

Output:

```
regional_analysis.csv
```

---

# 🚀 Running the Project

## 1️⃣ Install Dependencies

Create virtual environment:

```
python -m venv .venv
```

Activate environment:

```
.venv\Scripts\activate
```

Install packages:

```
pip install fastapi uvicorn pandas
```

---

# 2️⃣ Run Data Cleaning

```
python backend/clean_data.py
```

---

# 3️⃣ Run Data Analysis

```
python backend/analyze.py
```

This generates processed datasets inside:

```
data/processed
```

---

# 4️⃣ Start Backend API

```
uvicorn backend.main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

---

# 🌐 API Endpoints

## Health Check

```
GET /health
```

Response:

```
{
 "status": "ok"
}
```

---

## Monthly Revenue

```
GET /api/revenue
```

---

## Top Customers

```
GET /api/top-customers
```

---

## Category Performance

```
GET /api/categories
```

---

## Regional Analysis

```
GET /api/regions
```

---

# 💻 Running Frontend Dashboard

Navigate to frontend folder:

```
cd frontend
```

Run simple server:

```
python -m http.server 5500
```

Open browser:

```
http://localhost:5500
```

---

# 📊 Dashboard Features

The dashboard displays:

* Monthly revenue
* Top customers
* Category performance
* Regional analysis

The frontend fetches data from the backend API using **JavaScript Fetch API**.

---

# 🔍 Example API Response

```
{
 "status": "success",
 "rows": 5,
 "data": [
  {
   "region": "North",
   "customers": 20,
   "orders": 45,
   "total_revenue": 12000,
   "avg_revenue_per_customer": 600
  }
 ]
}
```

---

# 🎯 Key Learning Outcomes

This project demonstrates:

* Real-world data pipeline
* Data cleaning using Pandas
* Data transformation and analysis
* REST API development with FastAPI
* Frontend integration with APIs
* Building a simple analytics dashboard

---

# 👨‍💻 Author

**Name:** Shalini Gupta
**Project:** Sales Data Pipeline & Dashboard
**Tech Stack:** Python, FastAPI, Pandas, HTML, CSS, JavaScript

---

# 📄 License

This project is created for educational and assignment purposes.
