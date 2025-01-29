import pandas as pd
import numpy as np
import datetime

# Generate sample real-time financial data
np.random.seed(42)
dates = pd.date_range(end=datetime.datetime.today(), periods=365, freq='D')
close_prices = np.cumsum(np.random.randn(365) * 2 + 150)  # Simulated stock prices
open_prices = close_prices + np.random.randn(365) * 2
high_prices = np.maximum(close_prices, open_prices) + np.random.rand(365) * 2
low_prices = np.minimum(close_prices, open_prices) - np.random.rand(365) * 2
volumes = np.random.randint(100000, 500000, size=365)

# Create DataFrame
financial_data = pd.DataFrame({
    'Date': dates,
    'Open': open_prices,
    'High': high_prices,
    'Low': low_prices,
    'Close': close_prices,
    'Volume': volumes
})

# Save the dataset
file_path = "/mnt/data/sample_financial_data.csv"
financial_data.to_csv(file_path, index=False)

# Display DataFrame to user
import ace_tools as tools
tools.display_dataframe_to_user(name="Sample Financial Data", dataframe=financial_data)

file_path