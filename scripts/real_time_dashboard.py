import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import openai

# Load financial data
df = pd.read_csv("data/processed/financial_data.csv")

# Streamlit dashboard
st.title("Real-time Financial Dashboard")

# Line chart of stock price
st.subheader("Stock Price Trend")
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.legend()
st.pyplot(plt)

# AI-Powered Financial Summary
st.subheader("AI-Generated Financial Summary")
openai.api_key = "your_openai_api_key"
prompt = f"Analyze the following financial data:\n{df.to_string()}"
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)
summary = response["choices"][0]["message"]["content"]
st.write(summary)