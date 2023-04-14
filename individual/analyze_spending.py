import datetime
from collections import defaultdict
import statistics

def parse_transactions(file_path):
    transactions = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            timestamp, username, category, amount = line.strip().split(" ")
            transaction_time = datetime.datetime.fromisoformat(timestamp)
            transactions.append((transaction_time, username, category, float(amount)))
    return transactions

def analyze_transactions(transactions):
    categories_amounts = defaultdict(list)
    time_diffs = []

    for i in range(len(transactions) - 1):
        _, _, category1, amount1 = transactions[i]
        time1, _, _, _ = transactions[i]
        time2, _, _, _ = transactions[i + 1]

        time_diff = (time2 - time1).total_seconds()
        time_diffs.append(time_diff)

        categories_amounts[category1].append(amount1)

    category_stats = {}
    for category, amounts in categories_amounts.items():
        mean = statistics.mean(amounts)
        stddev = statistics.stdev(amounts)
        category_stats[category] = (mean, stddev)

    mean_time_diff = statistics.mean(time_diffs)
    stddev_time_diff = statistics.stdev(time_diffs)

    anomalies = []

    for i in range(len(transactions)):
        time, username, category, amount = transactions[i]
        mean_amount, stddev_amount = category_stats[category]

        if i < len(transactions) - 1:
            time_diff = time_diffs[i]
        else:
            time_diff = None

        if amount > mean_amount + 2 * stddev_amount or (amount != round(amount, 0)):
            anomalies.append((time, username, category, amount, "High amount or decimal value"))

        if time_diff is not None and time_diff < mean_time_diff - 2 * stddev_time_diff:
            anomalies.append((time, username, category, amount, "Quick transactions"))

    return anomalies

if __name__ == "__main__":
    transactions = parse_transactions("logs3.txt")
    anomalies = analyze_transactions(transactions)

    print ("running")

    for anomaly in anomalies:
        print(f"Anomaly: {anomaly}")
