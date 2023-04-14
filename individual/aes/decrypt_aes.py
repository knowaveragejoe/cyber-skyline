# Import necessary libraries
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from datetime import datetime, timedelta
import time, hashlib

# Function to decrypt the ciphertext with a given key
def decrypt_file(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_data
    except ValueError:
        return None

# Encrypted file path, IV, and starting date
encrypted_file_path = "ciphertext"
# iv = b'your_iv_here'  # Replace with your initialization vector (IV)
start_date = "2023-01-01"  # Replace with the given starting date

# Read the encrypted file
with open(encrypted_file_path, "rb") as file:
    iv = file.read(16)  # Read the first 16 bytes as the IV
    ciphertext = file.read()

# Convert the starting date to UNIX timestamp
start_timestamp = int(time.mktime(datetime.strptime(start_date, "%Y-%m-%d").timetuple()))

# Iterate through all UNIX timestamps from the starting date
while True:
    # Generate a key from the current UNIX timestamp
    passphrase = str(start_timestamp).encode('utf-8')
    key = hashlib.sha256(passphrase).digest()

    print ("Trying passphrase:", passphrase)
    # Try to decrypt the file using the current key
    decrypted_data = decrypt_file(ciphertext, key, iv)


    # If the decryption was successful, save the decrypted file and exit the loop
    if decrypted_data is not None:
        print(decrypted_data.decode('iso-8859-1'))
        print(decrypted_data.hex())
        with open("decrypted_file.bin", "wb") as file:
            file.write(decrypted_data)
        print("Decryption successful. Passphrase found:", passphrase)
        break
    
    start_timestamp += 1