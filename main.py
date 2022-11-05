import cv2
from icecream import ic
import os
from dotenv import load_dotenv

load_dotenv()

# OPENCV:  BLUE GREEN RED
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (0, 0, 255, 255)

ORIGINAL_PIC = os.getenv("ORIGINAL_PIC")
STARS_ONLY_PIC = os.getenv("STARS_ONLY_PIC")
METEORS_ONLY_PIC = os.getenv("METEORS_ONLY_PIC")
DOTS_ONLY_PIC = os.getenv("DOTS_ONLY_PIC")
LOW_ALPHA_ONLY_PIC = os.getenv("LOW_ALPHA_ONLY_PIC")


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


def dotsOnly(picture, output):
    xsz, ysz = picture.shape[:2]
    temp = picture
    for x in range(xsz):
        for y in range(ysz):
            (_, _, r, _) = temp[x, y]
            if r >= 200:
                temp[x, y] = BLACK
            else:
                temp[x, y] = WHITE
    cv2.imwrite(output, temp)


def zeroAplhaOnly(picture, output):
    xsz, ysz = picture.shape[:2]
    temp = picture
    for x in range(xsz):
        for y in range(ysz):
            (_, _, _, a) = temp[x, y]
            if a < 255:
                temp[x, y] = BLACK
            else:
                temp[x, y] = WHITE
    cv2.imwrite(output, temp)


def fillNeighbors(pic, xsz, ysz, x, y):
    (b, g, r, _) = pic[x, y]
    if (b, g, r, _) == WHITE:
        return
    pic[x, y] = WHITE
    if x > 0:
        fillNeighbors(pic, xsz, ysz, x - 1, y)
    if x < xsz - 1:
        fillNeighbors(pic, xsz, ysz, x + 1, y)
    if y > 0:
        fillNeighbors(pic, xsz, ysz, x, y - 1)
    if y < xsz - 1:
        fillNeighbors(pic, xsz, ysz, x, y + 1)


def countStars(picture):
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


def xLen(pic, xsz, x, y):
    if x >= xsz:
        return 0
    (b, g, r, _) = pic[x, y]
    if (b, g, r, _) == WHITE:
        return 0
    return 1 + xLen(pic, xsz, (x + 1), y)


def yLen(pic, ysz, x, y):
    if y >= ysz:
        return 0
    (b, g, r, _) = pic[x, y]
    if (b, g, r, _) == WHITE:
        return 0
    return 1 + yLen(pic, ysz, x, y + 1)


def countMeteors(picture):
    count = hCount = 0
    picture
    xsz, ysz = picture.shape[:2]
    for y in range(ysz):
        for x in range(xsz):
            (b, g, r, _) = picture[x, y]
            if (b, g, r, _) == RED:
                count += 1
                if yLen(picture, ysz, x, y) > xLen(picture, xsz, x, y):
                    hCount += 1
                fillNeighbors(picture, xsz, ysz, x, y)
    return count, hCount


# -1 for transparency channel
pic = cv2.imread(ORIGINAL_PIC, -1)
starsOnly(pic, STARS_ONLY_PIC)
ic(countStars(cv2.imread(STARS_ONLY_PIC, -1)))

pic = cv2.imread(ORIGINAL_PIC, -1)
meteorsOnly(pic, METEORS_ONLY_PIC)
ic(countMeteors(cv2.imread(METEORS_ONLY_PIC, -1)))

pic = cv2.imread(ORIGINAL_PIC, -1)
dotsOnly(pic, DOTS_ONLY_PIC)

pic = cv2.imread(ORIGINAL_PIC, -1)
zeroAplhaOnly(pic, LOW_ALPHA_ONLY_PIC)
