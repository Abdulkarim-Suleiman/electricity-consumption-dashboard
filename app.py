import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("electricity_consumption_by_area-sector_2012-2018.csv")

# Preprocess
df["year"] = df["year"].astype(str)
df["Sector_Share"] = df.groupby("year")["Consumption"].transform(lambda x: x / x.sum() * 100)
df_sorted = df.sort_values(["Area", "Sector", "year"])
df_sorted["YoY_Change"] = df_sorted.groupby(["Area", "Sector"])["Consumption"].pct_change() * 100

# Sidebar filters
st.sidebar.header("🔍 Filter Data")
year_filter = st.sidebar.multiselect("Select Year(s):", options=df["year"].unique(), default=df["year"].unique())
area_filter = st.sidebar.multiselect("Select Area(s):", options=df["Area"].unique(), default=df["Area"].unique())
sector_filter = st.sidebar.multiselect("Select Sector(s):", options=df["Sector"].unique(), default=df["Sector"].unique())

# Filtered data
filtered_df = df[df["year"].isin(year_filter) & df["Area"].isin(area_filter) & df["Sector"].isin(sector_filter)]

# Title
st.title("⚡ Electricity Consumption Dashboard: UAE (2012–2018)")
st.markdown("Explore consumption by **sector**, **area**, and **year**. Built with Streamlit and Plotly.")

# KPIs
st.subheader("📌 Key Performance Insights")
col1, col2, col3 = st.columns(3)
col1.metric("Max Consumption (GWh)", f"{filtered_df['Consumption'].max():,.0f}")
col2.metric("Min Consumption (GWh)", f"{filtered_df['Consumption'].min():,.0f}")
col3.metric("Avg. Year-over-Year Change", f"{df_sorted['YoY_Change'].mean():.2f} %")

# Line chart - Trend by Sector
st.subheader("📈 Consumption Trend by Sector")
fig1 = px.line(filtered_df, x="year", y="Consumption", color="Sector", markers=True)
st.plotly_chart(fig1)

# Stacked Area - Sector Share
st.subheader("📊 Sector Share Over Time")
share_df = filtered_df.groupby(["year", "Sector"])["Sector_Share"].mean().reset_index()
fig2 = px.area(share_df, x="year", y="Sector_Share", color="Sector", groupnorm='percent')
st.plotly_chart(fig2)

# Grouped Bar - Area Comparison
st.subheader("🏙️ Consumption by Sector and Area")
fig3 = px.bar(filtered_df, x="Sector", y="Consumption", color="Area", barmode="group")
st.plotly_chart(fig3)

# Data Table
st.subheader("📋 Filtered Data Table")
st.dataframe(filtered_df.sort_values(by=["year", "Area", "Sector"]))
