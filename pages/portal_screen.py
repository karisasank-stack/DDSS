import streamlit as st
import pandas as pd

st.title("🏭 PORTAL SCREEN")

# Read CSV
df = pd.read_csv("data/supplier_delivery.csv")

# Calculate accuracy and risk
summary = []

for supplier in df["Supplier_Name"].unique():

    supplier_df = df[df["Supplier_Name"] == supplier]

    total = len(supplier_df)

    on_time = (
        supplier_df["Actual_Delivery_Time"]
        <= supplier_df["Planned_Delivery_Time"]
    ).sum()

    accuracy = round((on_time / total) * 100, 0)

    risk = 100 - accuracy

    summary.append(
        {
            "Supplier": supplier,
            "Accuracy (%)": accuracy,
            "Risk (%)": risk
        }
    )

result = pd.DataFrame(summary)

st.dataframe(result, use_container_width=True)