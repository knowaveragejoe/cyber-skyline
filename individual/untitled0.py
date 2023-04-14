# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yIgabmhjaPBEB4nmTOx-U5T5YVUwBOJ7
"""

import pandas as pd
import matplotlib.pyplot as plt

# read log file into pandas dataframe
df = pd.read_csv('logs3.txt', sep=' ', header=None, names=['datetime', 'name', 'type', 'amount'])

# convert datetime column to datetime format
df['datetime'] = pd.to_datetime(df['datetime'])

# plot total amount by date
df.groupby(df['datetime'].dt.date)['amount'].sum().plot(kind='bar', figsize=(10, 5))
plt.xlabel('Date')
plt.ylabel('Total Amount')
plt.title('Total Amount by Date')
plt.show()

# plot total amount by name
df.groupby('name')['amount'].sum().sort_values().plot(kind='barh', figsize=(10, 5))
plt.xlabel('Total Amount')
plt.title('Total Amount by Name')
plt.show()

# plot total amount by type
df.groupby('type')['amount'].sum().sort_values().plot(kind='barh', figsize=(10, 5))
plt.xlabel('Total Amount')
plt.title('Total Amount by Type')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Read the log file into a pandas DataFrame
df = pd.read_csv('logs3.txt', sep=' ', header=None, names=['timestamp', 'username', 'category', 'amount'])

# Convert the timestamp to a datetime object and set it as the index
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Group the data by category and resample it to daily frequency
daily_totals = df.groupby('category')['amount'].resample('D').sum().unstack()

# Plot the total amount spent in each category over time
daily_totals.plot(kind='area', stacked=False, alpha=0.5)
plt.xlabel('Date')
plt.ylabel('Total Amount Spent')
plt.title('Total Amount Spent by Category')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


# read log file into pandas dataframe
df = pd.read_csv('logs3.txt', sep=' ', header=None, names=['datetime', 'name', 'category', 'amount'])

# convert datetime column to datetime format
df['datetime'] = pd.to_datetime(df['datetime'])

# Create a pivot table to aggregate the data by category and datetime
table = pd.pivot_table(df, values='amount', index='datetime', columns='category', aggfunc='sum')

# Plot the data
ax = table.plot(figsize=(10, 6), legend=False)

for col in table.columns:
    highest_val = table[col].max()
    highest_date = table[col].idxmax()
    ax.annotate(f'{col}: {highest_val}', xy=(highest_date, highest_val), xytext=(highest_date, highest_val+10), arrowprops=dict(facecolor='black', arrowstyle='->'))

# Set plot properties
plt.xlabel('Datetime')
plt.ylabel('Amount')
plt.title('Transactions by Category over Time')

# Display the plot
plt.show()

import pandas as pd
import datetime

def parse_log_line(line):
    timestamp_str, username, category, amount = line.strip().split()
    timestamp = datetime.datetime.fromisoformat(timestamp_str)
    amount = float(amount)
    return timestamp, username, category, amount

def is_unusual(transaction, threshold=100):
    return transaction["amount"] > threshold


purchase_data = []

with open("logs3.txt", "r") as f:
    for line in f:
        purchase_data.append(parse_log_line(line))

df = pd.DataFrame(purchase_data, columns=["timestamp", "username", "category", "amount"])

import matplotlib.pyplot as plt

def plot_purchase_data(df):
    fig, ax = plt.subplots(figsize=(15, 8))
    
    df.plot(x="timestamp", y="amount", kind="line", ax=ax)
    
    unusual_transactions = df[df.apply(is_unusual, axis=1)]
    for _, transaction in unusual_transactions.iterrows():
        ax.annotate(
            f"{transaction['username']}, {transaction['category']}, {transaction['amount']}",
            (transaction["timestamp"], transaction["amount"]),
            textcoords="offset points",
            xytext=(0, 5),
            ha="center",
            fontsize=8,
            color="red",
        )

    plt.title("Purchase Amounts Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Amount")
    plt.grid()
    plt.show()

plot_purchase_data(df)

spending_by_category = df.groupby(["username", "category"]).sum().reset_index()

pivot_table = spending_by_category.pivot_table(
    index="username", columns="category", values="amount", fill_value=0
)
def plot_spending_by_category(pivot_table):
    ax = pivot_table.plot(kind="bar", stacked=True, figsize=(15, 8))

    plt.title("Spending per Category for Each Username")
    plt.xlabel("Username")
    plt.ylabel("Spending")
    plt.legend(title="Category", loc="upper left", bbox_to_anchor=(1, 1))
    plt.grid(axis="y")
    plt.show()

plot_spending_by_category(pivot_table)

import numpy as np

def plot_single_category_transactions(single_category_transactions):
    fig, ax = plt.subplots(figsize=(15, 8))

    unique_users = single_category_transactions["username"].unique()
    colors = plt.cm.get_cmap("tab10", len(unique_users))

    for i, user in enumerate(unique_users):
        user_transactions = single_category_transactions[single_category_transactions["username"] == user]
        ax.scatter(user_transactions["timestamp"], user_transactions["amount"], c=[colors(i)], label=user)

    ax.set_title("Transactions Over Time for Users with Only One Category of Spending")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Amount")
    ax.legend(title="Username", loc="upper left", bbox_to_anchor=(1, 1))
    ax.grid()

    plt.show()

plot_single_category_transactions(single_category_transactions)

def plot_single_category_transactions_line(single_category_transactions):
    fig, ax = plt.subplots(figsize=(15, 8))

    unique_users = single_category_transactions["username"].unique()
    colors = plt.cm.get_cmap("tab10", len(unique_users))

    for i, user in enumerate(unique_users):
        user_transactions = single_category_transactions[single_category_transactions["username"] == user]
        user_transactions = user_transactions.sort_values(by="timestamp")
        ax.plot(user_transactions["timestamp"], user_transactions["amount"], label=user, color=colors(i), marker="o")

    ax.set_title("Transactions Over Time for Users with Only One Category of Spending")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Amount")
    ax.legend(title="Username", loc="upper left", bbox_to_anchor=(1, 1))
    ax.grid()

    plt.show()

plot_single_category_transactions_line(single_category_transactions)

"""# New Section"""