import pandas as pd
import numpy as np
import os

np.random.seed(42)

# Ensure the folder exists
os.makedirs("data/raw", exist_ok=True)

# ---------------------------
# Orders (Shopify-style)
# ---------------------------
orders = pd.DataFrame({
    "order_id": range(1001, 2001),  # 1000 orders
    "customer_id": np.random.randint(1, 200, 1000),
    "order_date": pd.date_range(start="2024-01-01", periods=1000, freq="h"),
    "order_amount": np.random.randint(20, 200, 1000),
    "status": np.random.choice(["created", "paid"], 1000)
})

# ---------------------------
# Payments (Stripe-style)
# ---------------------------
payments = pd.DataFrame({
    "payment_id": range(5001, 6001),  # 1000 payments
    "order_id": np.random.choice(orders["order_id"], 1000),
    "payment_date": pd.date_range(start="2024-01-01 01:00", periods=1000, freq="h"),
    "amount_paid": np.random.randint(20, 200, 1000)
})

# Introduce mismatch: some orders have no payments
payments = payments.sample(frac=0.8, random_state=42)

# ---------------------------
# Ad Spend (Meta/Google)
# ---------------------------
ad_spend = pd.DataFrame({
    "date": pd.date_range(start="2024-01-01", periods=1000, freq="h"),
    "channel": np.random.choice(["Meta", "Google"], 1000),
    "spend": np.random.randint(50, 300, 1000)
})

# ---------------------------
# Expenses
# ---------------------------
expenses = pd.DataFrame({
    "date": pd.date_range(start="2024-01-01", periods=1000, freq="h"),
    "expense_type": np.random.choice(["COGS", "Shipping", "Tools"], 1000),
    "amount": np.random.randint(10, 150, 1000)
})

# ---------------------------
# Save files
# ---------------------------
orders.to_csv("data/raw/orders.csv", index=False)
payments.to_csv("data/raw/payments.csv", index=False)
ad_spend.to_csv("data/raw/ad_spend.csv", index=False)
expenses.to_csv("data/raw/expenses.csv", index=False)

print("Datasets created in data/raw/ folder.")