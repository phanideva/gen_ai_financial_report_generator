import pandas as pd
import yfinance as yf

def fetch_financial_data(ticker):
    """Fetch stock market financial data from Yahoo Finance."""
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    hist.reset_index(inplace=True)
    return hist

def preprocess_data(df):
    """Clean and preprocess financial data."""
    df = df.dropna()
    df['Date'] = pd.to_datetime(df['Date'])
    return df

if __name__ == "__main__":
    ticker = "AAPL"  # Example: Apple Stock
    data = fetch_financial_data(ticker)
    processed_data = preprocess_data(data)
    processed_data.to_csv("data/processed/financial_data.csv", index=False)
    print("Financial data saved successfully!")