#!/usr/bin/env python3

with open("logs3.txt", "r") as file:
    for line in file:
        fields = line.split()
        amount = int(fields[-1])
        if amount > 100:
            print(line.strip())