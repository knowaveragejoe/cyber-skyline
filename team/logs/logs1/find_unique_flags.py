import re

file_path = 'messages.txt'  # Replace with the path to your file
pattern = r'SKY-PGPG-(\d+)'  # Replace with the pattern you want to search for

counter = 0000

# Read the file line by line
with open(file_path, 'r', encoding='utf-8') as file:
    for line_number, line in enumerate(file, start=1):
        # print (counter) 
        match = re.search(pattern, line)
        if match:
            # print("Match: ", str(match.group(1)), "Counter: ", "{:04d}".format(counter))
            # print (match.group(1) == "{:04d}".format(counter))
            if match.group(1) == "{:04d}".format(counter):
                # print ("matches")
                pass
            else:
                print ("does not match")


            counter += 1
            #     # flag string matches our expected pattern
            #     print ("matches expected pattern")
            #     continue
            # else:
            #     # flag string does not match our expected pattern
            #     print("Flag does not match counter {} with value {}".format("{:04d}".format(counter), match.group(1)))