import re

# Define regular expressions to search for
suspicious_patterns = [
    r"\bpassword\b",
    r"\baccount\b",
    r"\blogin\b",
    r"\bverify\b",
    r"\bsecurity\b",
    r"\bfraud\b",
    r"\bphish\b",
    r"\bspoof\b",
    r"\bscam\b",
    r"\bsuspicious\b",
]

# Open the log file for reading
with open("logs2.txt", "r") as f:
    for line in f:
        # Check if any of the suspicious patterns appear in the line
        for pattern in suspicious_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                print("WARNING: Suspicious email detected!")
                print(line)
                break