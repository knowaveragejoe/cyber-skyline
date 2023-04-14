import plistlib
import base64

def read_plist_file(file_path):
    with open(file_path, 'r') as file:
        plist_data = file.read()
    return plist_data

def extract_base64_data(plist_data):
    start = plist_data.find("<data>") + len("<data>")
    end = plist_data.find("</data>")
    base64_data = plist_data[start:end].strip()
    return base64_data

def extract_font_details(base64_data):
    decoded_data = base64.b64decode(base64_data)
    deserialized_data = plistlib.loads(decoded_data)
    
    print(deserialized_data)
    
    # return font_details

# Read plist data from a file
file_path = "fruit.plist.xml"
plist_data = read_plist_file(file_path)

# Extract Base64-encoded data from plist data
base64_data = extract_base64_data(plist_data)

# Extract font details from Base64-encoded data
extract_font_details(base64_data)

# print("Font Details:")
# for key, value in font_details.items():
#     print(f"{key}: {value}")
