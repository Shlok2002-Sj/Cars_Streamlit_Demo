import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("CARS.csv")

# Title
st.title("🚗 Car Dataset Explorer")

# Sidebar Filters
st.sidebar.header("🔎 Filters")

# Brand filter
brand = st.sidebar.selectbox("Select Brand:", ["All"] + list(df["Make"].unique()))

# Year filter (if available in dataset)
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

# Summary stats
st.subheader("🔹 Summary Statistics")
st.write(df.describe(include="all"))

# Horsepower plot
if not df.empty:
    st.subheader("⚡ Horsepower by Model")
    fig, ax = plt.subplots(figsize=(10, 6))
    sb.barplot(x="Model", y="Horsepower", data=df, ax=ax, palette="viridis")
    plt.xticks(rotation=90)
    st.pyplot(fig)

    # Distribution plot
    st.subheader("📈 Horsepower Distribution")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sb.histplot(df["Horsepower"], kde=True, bins=20, ax=ax2, color="orange")
    st.pyplot(fig2)
else:
    st.warning("No cars match your filter selection.")
