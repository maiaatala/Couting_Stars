import cv2
from . import fillNeighbors

# OPENCV:  BLUE GREEN RED
WHITE = (255, 255, 255, 255)
RED = (0, 0, 255, 255)


def meteorsOnly(picture, output):
    xsz, ysz = picture.shape[:2]
    temp = picture
    for x in range(xsz):
        for y in range(ysz):
            (b, g, r, _) = temp[x, y]
            if (b, g, r, _) == RED:
                temp[x, y] = RED
            else:
                temp[x, y] = WHITE
    cv2.imwrite(output, temp)
    return picture


def countMeteors(picture, output):
    picture = meteorsOnly(picture, output)
    count = hCount = 0
    picture
    xsz, ysz = picture.shape[:2]
    for y in range(ysz):
        for x in range(xsz):
            (b, g, r, _) = picture[x, y]
            if (b, g, r, _) == RED:
                count += 1
                # fillNeighbors(picture, xsz, ysz, x, y)
    return count, hCount
