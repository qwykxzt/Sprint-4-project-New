import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
@st.cache_data
def load_data():
return pd.read_csv("vehicles_us.csv")

car_datasets = load_data()

# Header
st.header("🚗 Vehicle Data Dashboard")

# Checkbox to filter outliers
remove_outliers = st.checkbox("Remove extreme price outliers")

if remove_outliers:
car_datasets = car_datasets[car_datasets["price"] < car_datasets["price"].quantile(0.99)]

# Histogram of model years
fig_hist = px.histogram(
car_datasets, 
x="model_year", 
nbins=30, 
title="Distribution of Vehicle Model Years"
)
st.plotly_chart(fig_hist)

# Scatter plot of model year vs price
fig_scatter = px.scatter(
car_datasets, 
x="model_year", 
y="price", 
opacity=0.5, 
title="Car Price vs. Model Year"
)
st.plotly_chart(fig_scatter)

st.write("✅ Data loaded successfully. Explore trends in vehicle prices and model years!")

