with open("chris_RGBA.txt", "r") as f:
    rgba_str = f.read()

rgba_list = rgba_str.split(", ")

with open("output.txt", "w") as f:
    for i in range(0, len(rgba_list), 4):
        r = int(rgba_list[i])
        g = int(rgba_list[i+1])
        b = int(rgba_list[i+2])
        a = int(rgba_list[i+3])

        if (r >= 0 and r <= 255) and (g >= 0 and g <= 255) and (b >= 0 and b <= 255) and (a >= 0 and a <= 255):
            try:
                char = chr(r) + chr(g) + chr(b) + chr(a)
                f.write(char)
            except:
                pass
