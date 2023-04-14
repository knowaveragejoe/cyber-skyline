from collections import defaultdict

def find_duplicate_transactions(file_path):
    transactions = defaultdict(list)
    duplicate_transactions = []

    with open(file_path, 'r') as file:
        for line in file:
            fields = line.strip().split()

            if len(fields) == 4:
                timestamp, username, category, price = fields
                transaction_key = (username, category, price)

                if transaction_key in transactions:
                    duplicate_transactions.append((timestamp, username, category, price))
                else:
                    transactions[transaction_key].append((timestamp, username, category, price))

    return duplicate_transactions

def main():
    transaction_log_file_path = 'transactions.txt'
    duplicate_transactions = find_duplicate_transactions(transaction_log_file_path)

    if duplicate_transactions:
        print('Duplicate transactions (same category and price):')
        for transaction in duplicate_transactions:
            print(transaction)
    else:
        print('No duplicate transactions were found.')

if __name__ == '__main__':
    main()
