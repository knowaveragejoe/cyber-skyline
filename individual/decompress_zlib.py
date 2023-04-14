import zlib

# Read the compressed data from the file
with open('36.zlib', 'rb') as f:
    compressed_data = f.read()

# Decompress the data using zlib
decompressed_data = zlib.decompress(compressed_data)

# Write the decompressed data to a file
with open('decompressed_data.txt', 'wb') as f:
    f.write(decompressed_data)
