#!/usr/bin/env python3

import csv, string

table = str.maketrans('', '', string.punctuation)

with open('tv_shows.csv', 'r') as input_file, open('tv_shows.txt', 'w') as output_file:
    reader = csv.reader(input_file)
    for row in reader:
        # Check if row has at least 2 columns
        if len(row) >= 2:
            # Get the second field and apply transformations
            field2 = row[1].strip().lower().replace(" ", "")
            field2 = field2.translate(table)
            # Write the transformed field to the output file
            for i in range(0, 1000):
                output_file.write(field2 + "{:02d}".format(i) + '\n')
