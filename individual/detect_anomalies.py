import pandas as pd
from datetime import datetime

# File containing the data
file_path = 'logs3.txt'

# Read the data into a Pandas DataFrame
df = pd.read_csv(file_path, sep=' ', names=['Timestamp', 'Name', 'Type', 'Amount'], parse_dates=['Timestamp'])

# Calculate mean and standard deviation of the transaction amounts
mean_amount = df['Amount'].mean()
std_amount = df['Amount'].std()

# Identify anomalous transactions
anomalies = df[df['Amount'].apply(lambda x: abs(x) > 100)]

# Print anomalous transactions
print(anomalies)