import re

file_path = 'iptable.log'
# regex pattern for LEN=(\d+)
length_pattern = r"LEN=(\d+)"
ip_pattern = r"SRC=(\d+\.\d+\.\d+\.\d+)"

total = 0
lengths = []
lengths_per_ip = {}
print("Logs are ", len(open(file_path).readlines(  )), " lines long")
with open(file_path, 'r', encoding='utf-8') as file:
    for line_number, line in enumerate(file, start=1):
        # match line on length_pattern
        length_match = re.search(length_pattern, line)
        if length_match:
            total += int(length_match.group(1))
            lengths.append(int(length_match.group(1)))
            src_match = re.search(ip_pattern, line)
            if src_match:
                if src_match.group(1) in lengths_per_ip:
                    lengths_per_ip[src_match.group(1)].append(int(length_match.group(1)))
                else:
                    lengths_per_ip[src_match.group(1)] = [int(length_match.group(1))]

    
print ("Total bytes trasnferred: ", total)
print ("Average bytes transferred: ", total/len(lengths))
print ("Max bytes transferred: ", max(lengths))
print ("Min bytes transferred: ", min(lengths))
print ("Max bytes transferred by IP: ")
# for ip in lengths_per_ip:
    # print ("IP: ", ip, " Max bytes transferred: ", max(lengths_per_ip[ip]))

sum_by_ip = 0
for ip in lengths_per_ip:
    sum_by_ip += sum(lengths_per_ip[ip])

print ("Average bytes transferred by IP: ", sum_by_ip/len(lengths_per_ip))