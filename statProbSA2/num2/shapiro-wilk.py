import pandas as pd
from scipy.stats import shapiro

# Load your data
data_path = 'ethereum_daily_returns.csv'
df = pd.read_csv(data_path)
returns = df['return'].dropna()

# Conduct the Shapiro-Wilk test
statistic, p_value = shapiro(returns)

print('Shapiro-Wilk Statistic:', statistic)
print('p-value:', p_value)
