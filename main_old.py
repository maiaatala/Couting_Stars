from PIL import Image
from icecream import ic

pic = Image.open("./meteor_challenge_01/meteor_challenge_01.png")

xsize, ysize = pic.size
bx = by = max_val = rx = ry = max_red = 0
lower_gb = 255 * 2

# ic(pic.getpixel((703, 703)))


for x in range(xsize):
    for y in range(ysize):
        r, g, b, _ = pic.getpixel((x, y))
        # Find brightest value
        if r + g + b > max_val:
            bx, by, max_val = x, y, r + g + b
        # find redest red.
        if r > max_red and g + b < lower_gb:
            rx, ry, max_red, lower_gb = x, y, r, b + g


ic(bx, by, max_val)
ic(rx, ry, max_red, lower_gb)
ic(pic.getpixel((rx, ry)))
