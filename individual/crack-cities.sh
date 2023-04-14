#!/usr/bin/env bash

while read -r city; do
    echo "Trying city: $city"
    hashcat -m 0 -a 6 cracking-4.txt nouns.txt "${city}?d?d" --username
done < /Users/jclark/tools/SecLists/Miscellaneous/us-cities.txt