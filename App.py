import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../DataSets/CARS.csv")

# Streamlit Title
st.title("Car Horsepower Comparison")

# Dropdown for brand selection
brand = st.selectbox("Select Car Brand:", df["Make"].unique())

# Filter dataset by selected brand
filtered_df = df[df["Make"] == brand]

# Create Seaborn barplot
fig, ax = plt.subplots(figsize=(10, 6))
sb.barplot(x="Model", y="Horsepower", data=filtered_df, ax=ax)
plt.xticks(rotation=90)

# Show plot in Streamlit
st.pyplot(fig)
