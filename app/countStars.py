import cv2
from . import fillNeighbors

# OPENCV:  BLUE GREEN RED
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)


def starsOnly(picture, output):
    xsz, ysz = picture.shape[:2]
    temp = picture
    for x in range(xsz):
        for y in range(ysz):
            (b, g, r, _) = temp[x, y]
            if (b, g, r, _) == WHITE:
                temp[x, y] = BLACK
            else:
                temp[x, y] = WHITE
    cv2.imwrite(output, temp)
    return picture


def countStars(picture, output):
    picture = starsOnly(picture, output)
    count = 0
    picture
    xsz, ysz = picture.shape[:2]
    for y in range(ysz):
        for x in range(xsz):
            (b, g, r, _) = picture[x, y]
            if (b, g, r, _) == BLACK:
                count += 1
                fillNeighbors(picture, xsz, ysz, x, y)
    return count
