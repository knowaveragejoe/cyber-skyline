def analyze_transaction_log(file_path):
    missing_fields_rows = []

    with open(file_path, 'r') as file:
        for line in file:
            fields = line.strip().split()

            if len(fields) != 4:
                missing_fields_rows.append(fields)

    return missing_fields_rows

def main():
    transaction_log_file_path = 'transactions.txt'
    missing_fields_rows = analyze_transaction_log(transaction_log_file_path)

    if missing_fields_rows:
        print('Rows with missing fields:')
        for row in missing_fields_rows:
            print(row)
    else:
        print('No rows with missing fields were found.')

if __name__ == '__main__':
    main()
