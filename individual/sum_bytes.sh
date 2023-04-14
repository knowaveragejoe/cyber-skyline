#!/bin/bash

log_file="logs1.txt"
total_bytes=0

while read -r line; do
  bytes=$(echo "$line" | awk '{print $10}')
  total_bytes=$((total_bytes + bytes))
done < "$log_file"

echo "Total bytes transferred: $total_bytes"