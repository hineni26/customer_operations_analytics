import streamlit as st
import pandas as pd

#Page title
st.title("Customer Operations Analytics Dashboard")

#Load data
df = pd.read_csv("data/cleaned_data.csv")

#show preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

#Now actual data
st.subheader("Key Operational KPIs")

col1, col2, col3=st.columns(3)
col1.metric("Total Tickets", len(df))
col2.metric("High Priority Tickets",(df["priority"]=="high").sum())
col3.metric("Top Support Queue",(df["queue"].value_counts()).head(1))

