import streamlit as st
import pandas as pd

#Page title
st.title("Customer Operations Analytics Dashboard")

#Page decription
st.markdown(
    """
    This dashboard analyzes customer support operations using 20K+ tickets.
    
    **Purpose:** Monitor workload distribution, priority trends, and support team performance to enable operational decision-making.
    """
)

#Load data
df = pd.read_csv("data/cleaned_data.csv")

##For filtering by priority
st.sidebar.header("Filters")

selected_priority = st.sidebar.selectbox(
    "Select Priority",
    options=["All"] + list(df["priority"].unique())
)



if selected_priority != "All":
    filtered_df = df[df["priority"] == selected_priority]
else:
    filtered_df = df


#show preview
st.subheader("Dataset Preview")
st.dataframe(filtered_df.head())


#Now actual data
st.subheader("Key Operational KPIs")

col1, col2, col3=st.columns(3)
col1.metric("Total Tickets", len(filtered_df))
col2.metric("High Priority Tickets",(filtered_df["priority"]=="high").sum())
col3.metric("Top Support Queue",(filtered_df["queue"].value_counts()).head(1))

##Ticket distribution by priority and support-team
col1, col2 = st.columns(2)

with col1:
    st.subheader("Priority Distribution")
    priority_counts = filtered_df["priority"].value_counts()
    st.bar_chart(priority_counts)

with col2:
    st.subheader("Queue Distribution")
    queue_counts = filtered_df["queue"].value_counts()
    st.bar_chart(queue_counts)



##Ticket distribution by Issue type
st.subheader("Ticket Distribution by Issue Type")
type_counts = filtered_df["type"].value_counts()
st.bar_chart(type_counts)
