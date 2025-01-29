import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_financials(file_path):
    """Perform financial data analysis."""
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Moving average
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['MA200'] = df['Close'].rolling(window=200).mean()
    
    # Plot the stock price
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.plot(df['Date'], df['MA50'], label='50-Day MA', linestyle='--')
    plt.plot(df['Date'], df['MA200'], label='200-Day MA', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.title('Stock Price Analysis')
    plt.show()

if __name__ == "__main__":
    analyze_financials("data/processed/financial_data.csv")