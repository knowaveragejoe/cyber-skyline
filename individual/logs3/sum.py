from collections import defaultdict

def count_transactions_per_user(file_path):
    transactions_count = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            fields = line.strip().split()

            if len(fields) == 4:
                timestamp, username, category, price = fields
                transactions_count[username] += 1

    return transactions_count

def main():
    transaction_log_file_path = 'transactions.txt'
    transactions_count = count_transactions_per_user(transaction_log_file_path)

    if transactions_count:
        print('Number of transactions per user:')
        for username, count in transactions_count.items():
            print(f'{username}: {count}')
    else:
        print('No transactions were found.')

if __name__ == '__main__':
    main()
