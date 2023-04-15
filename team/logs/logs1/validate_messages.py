import pgpy

public_key_files = ['person1.pgp', 'person2.pgp', 'person3.pgp']  # Replace with your public key file paths

# Read public keys from files
public_keys = []
for key_file in public_key_files:
    public_key, _ = pgpy.PGPKey.from_file(key_file)
    public_keys.append(public_key)

messages_file = 'messages.txt'  # Replace with the path to the file containing signed PGP messages
message_delimiter = '-----END PGP SIGNED MESSAGE-----'

# Read messages from file
with open(messages_file, 'r') as mf:
    raw_data = mf.read()
    messages = raw_data.split(message_delimiter)

# Remove the last empty message after splitting
if not messages[-1].strip():
    messages.pop()

# Append the delimiter back to each message (except the last one)
for i in range(len(messages) - 1):
    messages[i] += message_delimiter

# Iterate over the messages and attempt to validate them using the public keys
for i, message in enumerate(messages, start=1):
    pgp_msg = pgpy.PGPMessage.from_blob(message)
    validation_success = False
    print ("Verifying message {}", i)

    for public_key in public_keys:
        try:
          if public_key.verify(pgp_msg):
              validation_success = True
              print(f'Message {i}: Signature validation successful using public key from {public_key_files[public_keys.index(public_key)]}')
              break
        except pgpy.errors.PGPError:
            pass

    if not validation_success:
        print(f'Message {i}: Signature validation failed using all provided public keys')
