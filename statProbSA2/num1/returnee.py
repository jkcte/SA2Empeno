import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Load your data
data_path = 'bitcoin_hourly_returns.csv'
df = pd.read_csv(data_path)
returns = df['return'].dropna()

# Perform KDE
kde = gaussian_kde(returns)

x = np.linspace(returns.min(), returns.max(), 1000)
density = kde(x)

plt.figure(figsize=(10, 6))
plt.plot(x, density, label='KDE')
plt.hist(returns, bins=50, density=True, alpha=0.5, label='Data Histogram')
plt.title('Kernel Density Estimation of Bitcoin Daily Returns')
plt.xlabel('Returns')
plt.ylabel('Density')
plt.legend()
plt.show()
