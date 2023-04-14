import pandas as pd
from datetime import datetime

def find_single_category_users(spending_by_category):
    user_counts = spending_by_category.groupby("username").size()
    single_category_users = user_counts[user_counts == 1].index.tolist()
    return single_category_users


def list_transactions_for_single_category_users(df, single_category_users):
    single_category_transactions = df[df["username"].isin(single_category_users)].sort_values(by="username")
    return single_category_transactions

df = pd.read_csv('logs3.txt', sep=' ', names=['timestamp', 'username', 'category', 'amount'], parse_dates=['timestamp'])

spending_by_category = df.groupby(["username", "category"]).sum().reset_index()

single_category_users = find_single_category_users(spending_by_category)
print("Usernames that only spend on one category:", single_category_users)

single_category_transactions = list_transactions_for_single_category_users(df, single_category_users)
print("Transactions for users with only one category of spending:")
print(single_category_transactions)