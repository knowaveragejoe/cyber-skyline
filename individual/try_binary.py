from PIL import Image

# Load the image
img = Image.open("chris.png")
width, height = img.size

# Get the first row of pixels
pixels = img.load()
first_row = [pixels[x, 0][0] for x in range(width)]

# Check if the red channel of the first row is a binary message
binary_message = ""
for pixel in first_row:
    if pixel == 255:
        binary_message += "1"
    elif pixel == 0:
        binary_message += "0"
    else:
        print("The first row of pixels does not contain a binary message")
        break

print("Binary message:", binary_message)
