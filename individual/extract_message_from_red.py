from PIL import Image

# Load the image
image = Image.open('chris.png')

# Get the pixel data
pixels = image.load()

# Extract the red component of the first row pixels
red_values = [pixels[x, 0][0] for x in range(image.width)]

# Convert the red values to ASCII characters
message = ''.join(chr(value) for value in red_values)

