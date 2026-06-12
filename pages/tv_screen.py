import streamlit as st
import pandas as pd

st.set_page_config(page_title="DDSS TV Screen", layout="wide")

st.title("🚚 DDSS TV SCREEN")

# Read CSV
df = pd.read_csv("data/supplier_delivery.csv")

# Generate status
status = []

for supplier in df["Supplier_Name"]:
    if supplier == "ASK AUTOMOTIVE":
        status.append("🟢 GREEN")
    elif supplier == "VARROC ENGINEERING":
        status.append("🔴 RED")
    else:
        status.append("🟡 YELLOW")

# Create TV screen table
tv_data = pd.DataFrame({
    "Lot": df["Lot_No"],
    "Status": status
})

# Display
st.dataframe(tv_data, use_container_width=True)