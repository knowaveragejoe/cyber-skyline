logfile = 'access.log'

total_bytes = 0

with open(logfile, 'r') as f:
    for line in f:
        fields = line.split()
        try:
            response_code = int(fields[8])
            response_size = int(fields[9])
            if response_code != 404:
                total_bytes += response_size
        except (IndexError, ValueError):
            # Skip malformed log lines
            continue

print(f'Total bytes transferred: {total_bytes}')