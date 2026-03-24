import json
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Test Dashboard", layout="wide")

st.title("🚀 Test Automation Dashboard")

# Load report
with open("reports/report.json") as f:
    data = json.load(f)

tests = data["tests"]

# Extract data
records = []
for test in tests:
    records.append({
        "name": test.get("nodeid", "unknown"),
        "outcome": test.get("outcome", "unknown"),
        "duration": test.get("duration", 0)
    })

df = pd.DataFrame(records)

# ---- Metrics ----
total = len(df)
passed = len(df[df["outcome"] == "passed"])
failed = len(df[df["outcome"] == "failed"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Tests", total)
col2.metric("Passed ✅", passed)
col3.metric("Failed ❌", failed)

# ---- Pie Chart ----
st.subheader("Test Result Distribution")
st.bar_chart(df["outcome"].value_counts())

# ---- Table ----
st.subheader("Test Details")
st.dataframe(df)

# ---- Slow tests ----
st.subheader("Slowest Tests")
slow_tests = df.sort_values(by="duration", ascending=False).head(5)
st.dataframe(slow_tests)