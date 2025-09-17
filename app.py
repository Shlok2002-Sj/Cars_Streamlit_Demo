import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("CARS.csv")

# Title
st.title("🚗 Car Dataset 3D Explorer")

# Sidebar Filters
st.sidebar.header("🔎 Filters")

# Brand filter
brand = st.sidebar.selectbox("Select Brand:", ["All"] + list(df["Make"].unique()))

# Year filter (if available)
if "Year" in df.columns:
    year_range = st.sidebar.slider(
        "Select Year Range:",
        int(df["Year"].min()), 
        int(df["Year"].max()), 
        (int(df["Year"].min()), int(df["Year"].max()))
    )
    df = df[(df["Year"] >= year_range[0]) & (df["Year"] <= year_range[1])]

# Body style filter (if available)
if "BodyStyle" in df.columns:
    body_styles = st.sidebar.multiselect(
        "Select Body Style(s):", df["BodyStyle"].unique()
    )
    if body_styles:
        df = df[df["BodyStyle"].isin(body_styles)]

# Apply brand filter
if brand != "All":
    df = df[df["Make"] == brand]

# Show dataset preview
st.subheader("📊 Filtered Dataset")
st.dataframe(df)

# 3D Scatter Plot (Horsepower vs Weight vs MPG)
if {"Horsepower", "Weight", "MPG"}.issubset(df.columns):
    st.subheader("🌐 3D Car Performance Visualization")
    fig = px.scatter_3d(
        df,
        x="Horsepower",
        y="Weight",
        z="MPG",
        color="Make",
        hover_data=["Model"],
        size="Horsepower",
        opacity=0.8,
    )
    st.plotly_chart(fig, use_container_width=True)

# Interactive bar chart
if "Horsepower" in df.columns:
    st.subheader("⚡ Average Horsepower by Brand")
    avg_hp = df.groupby("Make")["Horsepower"].mean().reset_index()
    fig2 = px.bar(
        avg_hp,
        x="Make",
        y="Horsepower",
        color="Horsepower",
        title="Average Horsepower per Brand",
    )
    st.plotly_chart(fig2, use_container_width=True)

# Histogram
if "Horsepower" in df.columns:
    st.subheader("📈 Horsepower Distribution")
    fig3 = px.histogram(df, x="Horsepower", nbins=20, color="Make")
    st.plotly_chart(fig3, use_container_width=True)
