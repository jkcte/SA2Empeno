import pandas as pd

# Load the data from CSV file
df = pd.read_csv('ethereum_daily_data.csv')

# Ensure the 'time' column is a datetime type
df['time'] = pd.to_datetime(df['time'])

# Sort the data by time in case it's not sorted
df = df.sort_values(by='time')

# Calculate returns using the price column. Assuming 'close' is the price at which the hour closed
df['return'] = df['close'].pct_change()

# Optionally, remove the first row since its return will be NaN (no previous price available)
df = df.dropna()

# Save the new dataframe with returns
df.to_csv('ethereum_daily_returns.csv', index=False)

# Print a snippet of the dataframe to check
print(df.head())