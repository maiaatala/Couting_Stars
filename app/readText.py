import cv2
import pytesseract

# OPENCV:  BLUE GREEN RED
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)


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


def readingTest(picture):
    text = pytesseract.image_to_string(picture)
    return text
