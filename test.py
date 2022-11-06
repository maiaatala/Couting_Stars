import cv2
from icecream import ic
import os
from dotenv import load_dotenv

# OPENCV:  BLUE GREEN RED
WHITE = (255, 255, 255, 255)
RED = (0, 0, 255, 255)
BLUE = (255, 0, 0, 255)
BLACK = (0, 0, 0, 255)


def minusRed(picture):
    xsz, ysz = picture.shape[:2]
    for x in range(xsz):
        for y in range(ysz):
            (b, g, r, _) = picture[x, y]
            if r > 0:
                r = 0
                picture[x, y] = (b, g, r, _)
    cv2.imwrite("./testOUTPUT/noBlue.png", picture)


def minusBlue(picture):
    xsz, ysz = picture.shape[:2]
    for x in range(xsz):
        for y in range(ysz):
            (b, g, r, _) = picture[x, y]
            if b > 0:
                b = 0
                picture[x, y] = (b, g, r, _)
    cv2.imwrite("./testOUTPUT/noRed.png", picture)


def minusGreen(picture):
    xsz, ysz = picture.shape[:2]
    for x in range(xsz):
        for y in range(ysz):
            (b, g, r, _) = picture[x, y]
            if g > 0:
                g = 0
                picture[x, y] = (b, g, r, _)
    cv2.imwrite("./testOUTPUT/noGreen.png", picture)


## image with black background and white dots
def starsMeteor(picture):
    xsz, ysz = picture.shape[:2]
    for x in range(xsz):
        for y in range(ysz):
            (b, g, r, _) = picture[x, y]
            if (b, g, r, _) != RED and (b, g, r, _) != WHITE:
                picture[x, y] = BLACK
                continue
            picture[x, y] = WHITE
    cv2.imwrite("./testOUTPUT/noBG.png", picture)
    return picture


# counts every dot in a line and tries to atribute an ascii value to them
def countMeteorsAndWaterMeteors(picture):
    picture = starsMeteor(picture)
    loopCount = lineCount = 0
    Letter = []
    xsz, ysz = picture.shape[:2]
    for x in range(ysz):
        loopCount = 0
        for y in range(xsz):
            (b, g, r, _) = picture[x, y]
            if r == 255:
                loopCount += 1
        lineCount += 1
        if lineCount < 2 or loopCount == 0:
            continue
        # the alphabet in the ascii table starts at 65
        Letter.append(chr(loopCount + 64))
        lineCount = 0

    return "".join(Letter)


load_dotenv()
ORIGINAL_PIC = os.getenv("ORIGINAL_PIC")

minusRed(cv2.imread(ORIGINAL_PIC, -1))
minusBlue(cv2.imread(ORIGINAL_PIC, -1))
minusGreen(cv2.imread(ORIGINAL_PIC, -1))


print(
    """ 
| Hidden Phrase: \n %s  |
"""
    % (countMeteorsAndWaterMeteors(cv2.imread(ORIGINAL_PIC, -1)))
)
